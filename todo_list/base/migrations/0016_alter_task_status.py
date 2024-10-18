# Generated by Django 5.1 on 2024-10-01 18:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0015_task_due_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='status',
            field=models.CharField(choices=[('not_started', 'Not Started'), ('in_progress', 'In Progress'), ('completed', 'Completed'), ('expired', 'Expired')], default='not_started', max_length=50),
        ),
    ]
