# Generated by Django 5.1 on 2024-09-25 11:03

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0014_remove_task_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='due_time',
            field=models.TimeField(default=datetime.time(12, 0)),
        ),
    ]
