# Generated by Django 4.1.2 on 2022-10-05 13:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0006_remove_task_type'),
    ]

    operations = [
        migrations.RenameField(
            model_name='task',
            old_name='tags',
            new_name='types',
        ),
    ]
