# Generated by Django 3.1.5 on 2021-01-25 21:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0005_remove_project_date_completed'),
    ]

    operations = [
        migrations.RenameField(
            model_name='task',
            old_name='task_autor',
            new_name='task_author',
        ),
    ]
