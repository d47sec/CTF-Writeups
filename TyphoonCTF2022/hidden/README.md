### SOLUTION

bypass login sử dụng username=admin&password[password]=1 

sau khi login thì có được source code của chall  [](app.js)

![](2022-06-25-09-57-59.png)

ta thấy đường dẫn của route này được gán với biến `${portasulretro}`


![](2022-06-25-09-59-37.png)

khi ta khi request đến route `/home` thì giá trị `${portasulretro}` sẽ được trả về trong header của response

ta thấy ở route `${portasulretro}` ta có thể thêm 1 param là kí tự hidden , và giá trị này sẽ được vào hàm `exec` mà không có filter gì => RCE 

![](2022-06-25-10-01-50.png)

