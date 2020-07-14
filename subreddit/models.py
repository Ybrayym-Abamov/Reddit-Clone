from django.db import models
from authentication.models import RedditUser


class Moderator(models.Model):
    is_moderator = models.BooleanField(default=False)
    user = models.ForeignKey(RedditUser, on_delete=models.CASCADE)
    def __str__(self):
        return self.user



class SubReddit(models.Model):
    name = models.CharField(max_length=30,unique=True)
    description = models.CharField(max_length=200)
    subscriber = models.ManyToManyField(RedditUser, related_name='user')
    moderator = models.ManyToManyField(Moderator, related_name='moderator')
    def __str__(self):
        return self.name