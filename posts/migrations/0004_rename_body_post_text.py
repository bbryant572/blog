# Generated by Django 4.0.3 on 2022-03-26 16:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0003_rename_text_post_body'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='body',
            new_name='text',
        ),
    ]