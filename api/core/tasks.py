from __future__ import absolute_import, unicode_literals
from celery.decorators import task, periodic_task
from celery.task.schedules import crontab
from . import models

@periodic_task(run_every=(crontab(minute='*/3')), name="check_seats", ignore_result=True)
def check_seats():
    for section in models.section.objects.filter(open_seats = False):
        section.update_seats()

@task(name="alert_all_users")
def alert_all_users(sect):
    for models.customUser in sect.customuser_set.all():
        print(str(customUser)) #TODO actually email/alert user here

@task(name="send_registration_email")
def send_registration_email(id):
    print("") #TODO actually email/alert user here
    