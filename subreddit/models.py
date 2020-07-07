from django.db import models
from authentication.models import RedditUser


class SubReddit(models.Model):
    name = models.CharField(default=30)
    description = models.CharField(default=200)
    subscriber = models.ManyToManyField(RedditUser, related_name='user')
    # posts
