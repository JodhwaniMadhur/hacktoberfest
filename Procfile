web: gunicorn -w 4 --chdir ./server/ app:app -b 127.0.0.1:$PORT
worker: gunicorn -w 4 --chdir ./server/ app:app -b 127.0.0.1:$PORT