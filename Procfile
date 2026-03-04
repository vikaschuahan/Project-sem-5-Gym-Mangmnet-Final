web: python manage.py migrate --noinput && python manage.py collectstatic --noinput && gunicorn GMS.wsgi --bind 0.0.0.0:$PORT --log-file -
