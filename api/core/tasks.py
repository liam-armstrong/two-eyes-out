from __future__ import absolute_import, unicode_literals
from celery.decorators import task, periodic_task
from celery import shared_task
from celery.task.schedules import crontab
from . import models
import logging
import redis

logger = logging.getLogger("celery")
client = redis.Redis(host="redis", port=6379, db=1)

@shared_task
def start_check_seats():
    logger.info("Running start_check_seats")
    length = client.llen("monitoring_queue")
    if length <= 0:
        for section in models.section.objects.all():
            update_seats.delay(id=section.id)
                    
@shared_task
def update_seats(id):
    if models.section.objects.get(id=id).update_seats():
        alert_all_users(id)

@shared_task
def alert_all_users(id):
    for user in models.section.objects.get(id=id).customuser_set.all():
        print(str(user)) #TODO actually email/alert user here
        #TODO DON'T FORGET TO SET SEAT AS INACTIVE FOR USER

@shared_task
def send_registration_email(user):
    print("Sending registration email to: " + str(user)) #TODO actually email/alert user here