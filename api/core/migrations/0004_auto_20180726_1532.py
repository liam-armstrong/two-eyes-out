# Generated by Django 2.0.7 on 2018-07-26 19:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_auto_20180726_1527'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userprofile',
            name='profile',
        ),
        migrations.DeleteModel(
            name='userProfile',
        ),
    ]
