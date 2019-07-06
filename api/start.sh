#!/bin/bash

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
        echo Starting Celery.
        exec celery -A api worker -l info
        ;;
    2) 
        echo Starting Celery Beat.
        exec celery -A api worker -l info
        ;;
    *)
		echo Incorrect START_CODE
		;;
    
esac

