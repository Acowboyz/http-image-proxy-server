# http-image-proxy-server

[![Build Status](https://travis-ci.org/Acowboyz/image-resizer.svg?branch=master)](https://travis-ci.org/Acowboyz/image-resizer)

1. return http status code 404 and emtpy page when APIs are not found.
    - flask

2. proxy api for image scaling to 500x500.
    - requests, pillow

3. admin api for number of times which proxy api is queried.
    - sqlite

4. optimize the query per second of web server
    - gunicorn, gevent
    
5. implement testing for production-ready
    - unit test
    

### TODO

- function documentation, nginx, docker, redis