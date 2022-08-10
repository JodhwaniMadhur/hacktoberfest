web: gunicorn -w 4 --chdir ./server/ wsgi:app -b 127.0.0.1:5000
worker: gunicorn -w 4 --chdir ./server/ wsgi:app -b 127.0.0.1:5000