# Generated by Django 5.1 on 2024-09-14 13:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0010_customuser_boi'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='location',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='customuser',
            name='phone_number',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
    ]
