1. POST /auth/login:

- scope: Không có scope
- lỗi & status code có thể xảy ra:

* thông tin gửi (request) invalid, không xử lý được - 400 Bad Request
* không thể authorize được (invalid credentials) 401 - 401 Unauthorized

- gửi request quá nhiều lần trong một thời gian nhất định - 429 Too Many Requests

2. POST /auth/refresh:

- scope: Không có scope
- lỗi & status code có thể xảy ra:

* thông tin gửi (request) invalid, không xử lý được - 400 Bad Request
* nội dung cửi (refresh token) không hợp lệ, không authorize được - 401 Unauthorized
* gửi request quá nhiều lần trong một thời gian nhất định - 429 Too Many Requests

3. GET /posts/{id}

- scope: read
- lỗi & status code có thể xảy ra:

* thiếu id hoặc viết sai định dạng id - 400 Bad Rquest
* thiếu access token - 401 Unauthorized
* client thiếu scope (read) - 403 Forbidden
* gửi request quá nhiều lần trong một thời gian nhất định - 429 Too Many Requests

4. Các điểm lộ có thể xảy ra:

- 'bruteforce' tại endpoint /auth/login mà không rate limit
- tái sử dụng refresh token: một người có thể sử dụng refresh token của người khác
- thiếu scope validation tại /posts/{id}
- thiếu expiration validation tại /auth/refresh
- rò rỉ database structure qua error responses
