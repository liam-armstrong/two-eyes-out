# Generated by Django 2.1.8 on 2019-06-29 17:08

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0009_auto_20190622_2010'),
    ]

    operations = [
        migrations.CreateModel(
            name='subscription',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_subscribed', models.DateField()),
                ('active', models.BooleanField(default=True)),
                ('premium', models.BooleanField(default=False)),
                ('section', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.section')),
            ],
        ),
        migrations.RemoveField(
            model_name='customuser',
            name='inactive_sections',
        ),
        migrations.RemoveField(
            model_name='customuser',
            name='sections'
        ),
        migrations.AddField(
            model_name='customuser',
            name='sections',
            field=models.ManyToManyField(through='core.subscription', to='core.section'),
        ),
        migrations.AddField(
            model_name='subscription',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
