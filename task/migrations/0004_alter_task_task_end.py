# Generated by Django 4.0.4 on 2022-06-21 07:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('task', '0003_alter_task_task_end'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='task_end',
            field=models.DateTimeField(default=models.DateTimeField(auto_now_add=True)),
        ),
    ]
