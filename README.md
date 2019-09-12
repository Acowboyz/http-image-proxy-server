# http-image-proxy-server

1. return http status code 404 and emtpy page when APIs are not found.
    - flask

2. proxy api for image scaling to 500x500.
    - requests, pillow

3. admin api for number of times which proxy api is queried.
    - sqlite

4. optimize the query per second of web server
    - gunicorn, gevent
    

### TODO

- unit test, function documentation, nginx, docker