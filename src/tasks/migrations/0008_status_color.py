# Generated by Django 4.1.2 on 2022-10-05 18:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0007_rename_tags_task_types'),
    ]

    operations = [
        migrations.AddField(
            model_name='status',
            name='color',
            field=models.CharField(default='#000', max_length=7, verbose_name='Цвет'),
            preserve_default=False,
        ),
    ]
