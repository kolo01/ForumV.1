# Generated by Django 5.1.1 on 2024-09-15 04:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Forum',
            new_name='ForumModel',
        ),
        migrations.RenameModel(
            old_name='Message',
            new_name='MessageModel',
        ),
        migrations.RenameModel(
            old_name='Sujet',
            new_name='TopicModel',
        ),
    ]
