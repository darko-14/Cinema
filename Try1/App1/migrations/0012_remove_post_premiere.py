# Generated by Django 3.0.4 on 2020-10-21 12:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('App1', '0011_dates'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='premiere',
        ),
    ]
