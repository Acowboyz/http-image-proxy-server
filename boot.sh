#!/usr/bin/env bash

host=127.0.0.1
port=5000

cat schema.sql | sqlite3 data.db
gunicorn -k gevent --worker-connections 100 -b ${host}:${port} http_image_proxy_server:app
#gunicorn http_image_proxy_server:aioapp -k aiohttp.worker.GunicornWebWorker --worker-connections 100 -b ${host}:${port}
#gunicorn -w 1 -b ${host}:${port} http_image_proxy_server:app