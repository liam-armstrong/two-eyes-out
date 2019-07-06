from __future__ import absolute_import, unicode_literals
from celery.decorators import task, periodic_task
from celery import shared_task
from celery.task.schedules import crontab
from . import models
import logging

logger = logging.getLogger("celery")

@periodic_task(run_every=(crontab(minute='*/3')), name="check_seats", ignore_result=True)
def check_seats():
    for section in models.section.objects.all():
        if section.update_seats():
                alert_all_users(section)

@shared_task
def alert_all_users(sect):
    for models.customUser in sect.customuser_set.all():
        print(str(customUser)) #TODO actually email/alert user here

@shared_task
def send_registration_email(user):
    print("") #TODO actually email/alert user here
    
@shared_task
def hello():
        print("Hello World")
        logger.info("-"*25)
        logger.info("Printing Hello from Celery")
        logger.info("-"*25)