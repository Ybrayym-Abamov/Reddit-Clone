from django.db import models
from django.contrib.auth.models import AbstractUser
from subreddit.models import SubReddit
# Create your models here.

class RedditUser(AbstractUser):
    karma = models.IntegerField(default=0)


class Moderator(models.Model):
    is_moderator = models.BooleanField(default=False)
    user = models.ForeignKey(RedditUser, on_delete=models.CASCADE)
    subreddit = models.ForeignKey(SubReddit, on_delete=models.CASCADE)