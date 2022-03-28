#!/bin/bash

RM=$(which rm)
${RM} -rf celerybeat-schedule  celerybeat-schedule.db
celery -A celery_app worker -B --loglevel=info
