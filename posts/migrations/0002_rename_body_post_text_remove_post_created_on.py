# Generated by Django 4.0.3 on 2022-03-25 19:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='body',
            new_name='text',
        ),
        migrations.RemoveField(
            model_name='post',
            name='created_on',
        ),
    ]
