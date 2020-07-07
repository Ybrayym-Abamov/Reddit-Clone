from django.db import models
from authentication.models import RedditUser


class Moderator(models.Model):
    is_moderator = models.BooleanField(default=False)
    user = models.ForeignKey(RedditUser, on_delete=models.CASCADE)
    subreddit = models.ForeignKey(SubReddit, on_delete=models.CASCADE)


class SubReddit(models.Model):
    name = models.CharField(max_length=30)
    description = models.CharField(max_length=200)
    subscriber = models.ForeignKey(RedditUser, on_delete=models.CASCADE,
                                   related_name='user')
    moderator = models.ForeignKey(Moderator, on_delete=models.CASCADE)
