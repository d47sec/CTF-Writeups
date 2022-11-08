## Endpoint ?page=shop 
sqli ở param type 

![](2022-11-08-00-22-58.png)


![](2022-11-08-00-23-52.png)

Từ đây là có thể đọc được flag ở trong table flags

## Endpoint ?page=user

Nếu có role=admin => thì nó sẽ gọi hàm preview 

![](2022-11-08-01-29-38.png)

Gọi đến hàm view

![](2022-11-08-01-30-09.png)
Sau đó gọi hàm preview_render() => nó sẽ load cái thư viện twig lên

![](2022-11-08-01-30-44.png)

Và hàm preview_render() này dính bug SSTI => thông qua tham số name => cái này ta hoàn toàn kiểm soát được 
![](2022-11-08-01-28-19.png)


RCE
payload: {{['whoami']|filter('system')}} 

![](2022-11-08-01-26-35.png)

Nhưng mà viễn cảnh này RCE chỉ diễn ra khi ta có role là admin :)) và rõ ràng là hiện tại ko có role là admin, default sẽ là user 

Vậy ta cần 1 bug nào đó để lợi dụng admin gửi POST request => CSRF, SSRF blalla .. hoặc ko có :))


![](2022-11-08-02-00-15.png)

Chỗ này có vẻ khả nghi nếu ta truy cập đến endpoint này từ local => đọc được /flag => có vẻ ssrf ở đây 

![](2022-11-08-02-54-46.png)

Ở đây mình ko biết giá trị của biến môi trường HOST_URL là gì nên đặt tạm =)))

Và với bug này thì ta có thể đọc được source code của đội khác => có được các thông tin liên quan TEAMSECRET,SALT,IV 

![](2022-11-08-02-57-05.png)


Nếu ta ko phải role admin thì sẽ nhảy vào nhánh if bên dưới 

![](2022-11-08-08-23-46.png)

Đoạn code này cho ta update, các giá trị thuộc tính của users 

Ý định của mình sẽ update role=admin và kết hợp bug ssti là thành RCE 

![](2022-11-08-08-26-11.png)


Nhưng ở đây nó sẽ ko cho update role :))

Vậy update cái khác thì sau ... 

Ở đây mình update luôn cái biến $guared, để mình có thể update role thành admin 

Đây là object user lúc ban đầu và lúc này role=user và guared=["role","username","money"] nên sẽ ko update đc role=admin ... 


![](2022-11-08-08-30-22.png)

Giờ mình sẽ update biến guared 
![](2022-11-08-08-33-00.png)

Đã update thành công :v , việc còn lại là khá dễ update role=admin thoi 

![](2022-11-08-08-34-05.png)


![](2022-11-08-08-37-06.png)

Pwned :v