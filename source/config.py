# -*- coding: utf-8 -*-

WEB_PORT = 9999

# Celery configuration
CELERY_BROKER_URL = 'redis://localhost:6379/1'
CELERY_RESULT_BACKEND = 'redis://localhost:6379/2'

