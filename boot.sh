#!/usr/bin/env bash

host=127.0.0.1
port=5000

gunicorn -k gevent -w 1 -b $host:$port http_image_proxy_server:app
