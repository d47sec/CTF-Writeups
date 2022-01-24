from pwn import *
r = remote('103.28.172.12',1111)

print(r.recvline())
print(r.recvline())
print(r.recvline())
print(r.recvline())
print(r.recvline())
print(r.recvline())

k = 1
while(k<=100):
  r.recvuntil(b':\n[')
  k=r.recvuntil(b']')

  kstr=str(k)
  print(kstr)
  f=kstr.replace("]","").replace(",","").replace("b","").replace("'","")
  arr=f.split()
  for i in range(0,len(arr)):
    arr[i]=int(arr[i])

  arr.sort()
  ans = str(arr)
  ans = ans.replace(",","")

  r.sendline(ans)
  
  k=k+1

r.interactive()

