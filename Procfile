web: gunicorn wsgi:application
worker: celery worker -A app.celery_tasks.celery_worker.celery --loglevel=info --pool=solo
