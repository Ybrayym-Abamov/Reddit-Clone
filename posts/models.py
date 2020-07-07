from django.db import models
from authentication.models import RedditUser
from subreddit.models import SubReddit
from comments.models import Comment
from django.utils import timezone


class Post(models.Model):
    title = models.CharField(default=150)
    body = models.CharField(default=4000)
    date_created = models.DateField(default=timezone.now)
    author = models.ForeignKey(RedditUser, on_delete=models.CASCADE)
    upvotes = models.IntegerField(default=0)
    downvotes = models.IntegerField(default=0)
    score = models.IntegerField(default=0)
    subreddit = models.ForeignKey(SubReddit, on_delete=models.CASCADE)
    comments = models.ManyToManyField(Comment, related_name='comments')


