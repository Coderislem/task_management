# Generated by Django 5.1 on 2024-10-05 08:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0016_alter_task_status'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='activitylog',
            name='task',
        ),
        migrations.AddField(
            model_name='activitylog',
            name='related_object',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
