### SOLUTION

Truy cập file robots.txt => ta có được 1 đường dẫn đến file php mới là `items.php` và nó nhận vào 1 param `sort` => có thể sqli

Sử dụng boolean based để leak data trên db 

[solve.py](solve.py)

có được username, password của admin đem đi login 
thì có chức năng upload file, nó không cho upload trực tiếp file .php 
có thể bypass bằng cách `ten_file.jpg.php` 

khả năng cao đoạn code kiểm tra extension server sẽ như sau.
```
extension = filename.explode(".")[1]
```

upload file [](shell.php) sau đó sử dụng burp để thay đổi tên name thành `shell.jpg.php` là có flag 

