# Generated by Django 4.0.4 on 2022-06-21 07:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0003_profile'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Profile',
            new_name='Mode',
        ),
    ]