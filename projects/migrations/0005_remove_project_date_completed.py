# Generated by Django 3.1.5 on 2021-01-25 20:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0004_auto_20210125_2055'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='project',
            name='date_completed',
        ),
    ]
