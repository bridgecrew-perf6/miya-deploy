from celery import Celery
from datetime import timedelta
from config import CELERY_BROKER_URL, CELERY_RESULT_BACKEND


app = Celery('celery_app', broker=CELERY_BROKER_URL, 
	backend=CELERY_RESULT_BACKEND,
	include=['celery_tasks'])
app.conf.update(
    CELERY_TASK_SERIALIZER='json',
    CELERY_IGNORE_RESULT=False,
    CELERYBEAT_SCHEDULE = {
        # 用于调试的任务,每隔一段时间执行一次
        'hello-every': {
            'task': 'celery_tasks.hello',
            'schedule': timedelta(seconds=10),
            'args': ('Hello World',)
        }        
	}
)

