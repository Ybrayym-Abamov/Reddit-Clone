# Generated by Django 3.0.8 on 2020-07-22 01:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0003_reddituser_subscribed'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='reddituser',
            name='subscribed',
        ),
    ]
