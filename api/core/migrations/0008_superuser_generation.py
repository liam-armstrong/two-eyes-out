# Generated by Django 2.1.1 on 2018-09-12 22:33

import os
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [('core', '0007_customuser_activated')]

    def generate_superuser(apps, schema_editor):
        from core.models import customUser

        DJANGO_SU_EMAIL = os.environ.get('DJANGO_SU_EMAIL')
        DJANGO_SU_PASSWORD = os.environ.get('DJANGO_SU_PASSWORD')
        
        superuser = customUser.objects.create_superuser(
            email=DJANGO_SU_EMAIL,  
            password=DJANGO_SU_PASSWORD)
        superuser.save()

    operations = [
        migrations.RunPython(generate_superuser),
]
