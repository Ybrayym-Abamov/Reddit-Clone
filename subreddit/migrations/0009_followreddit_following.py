# Generated by Django 3.0.8 on 2020-07-22 00:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('subreddit', '0008_followreddit'),
    ]

    operations = [
        migrations.AddField(
            model_name='followreddit',
            name='following',
            field=models.BooleanField(default=False),
        ),
    ]
