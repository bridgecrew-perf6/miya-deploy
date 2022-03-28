from celery import Celery

import celery_config
from config import CELERY_BROKER_URL, CELERY_RESULT_BACKEND

broker = CELERY_BROKER_URL
backend = CELERY_RESULT_BACKEND
app = Celery(
    'celery_app',
    broker=broker,
    backend=backend,
    include=['celery_tasks'])

app.config_from_object(celery_config)
