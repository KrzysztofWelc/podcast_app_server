web: gunicorn wsgi:application 0.0.0.0:$PORT
worker: celery worker -A app.celery_tasks.celery_worker.celery --loglevel=info --pool=solo
