# coding=utf-8
from celery.bin import worker as celery_worker

from celery_app import app


def worker_start():
    worker = celery_worker.worker(app=app)
    worker.run(concurrency=4, traceback=False, loglevel='INFO')


if __name__ == "__main__":
    worker_start()
