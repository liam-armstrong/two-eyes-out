#!/bin/bash
#! CELERY WORKER LOG LEVELS: DEBUG, INFO, WARNING, ERROR, CRITICAL, or FATAL.

echo Starting a Python container with START_CODE: ${START_CODE}

case ${START_CODE} in
	0)
        echo Starting Gunicorn.
        exec gunicorn api.wsgi:application \
            --bind 0.0.0.0:8000 \
            --workers 3 \
            --reload
        ;;
    1) 
        echo Starting Celery worker for default_queue.
        exec celery -A api worker -Q default_queue,monitoring_queue,trigger_queue -l INFO -n default_queue
        ;;
    2) 
        echo Starting Celery worker for monitoring_queue.
        exec celery -A api worker -Q monitoring_queue -l INFO -n monitoring_worker
        ;;
    3) 
        echo Starting Celery worker for trigger_queue.
        exec celery -A api worker -Q trigger_queue -l INFO -n trigger_worker
        ;;
    4) 
        echo Starting Celery worker for Celery Beat.
        exec celery -A api beat -l INFO
        ;;
    *)
		echo Incorrect START_CODE= ${START_CODE}
		;;
    
esac

