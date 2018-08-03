# Generated by Django 2.1 on 2018-08-03 18:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_section_seats'),
    ]

    operations = [
        migrations.AddField(
            model_name='section',
            name='open_seats',
            field=models.BooleanField(default=False),
        ),
        migrations.RemoveField(
            model_name='section',
            name='seats',
        ),
        migrations.AlterUniqueTogether(
            name='section',
            unique_together={('dept', 'code', 'sect')},
        ),
    ]
