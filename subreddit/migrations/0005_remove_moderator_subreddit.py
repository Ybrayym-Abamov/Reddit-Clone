# Generated by Django 3.0.8 on 2020-07-08 19:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('subreddit', '0004_auto_20200708_1942'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='moderator',
            name='subreddit',
        ),
    ]