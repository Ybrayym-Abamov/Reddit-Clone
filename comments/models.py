from django.db import models
from mptt.models import MPTTModel, TreeForeignKey
from django.utils import timezone
from posts.models import Post
from authentication.models import RedditUser


class Comment(MPTTModel):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    body = models.TextField(max_length=4000)
    user = models.ForeignKey(RedditUser, on_delete=models.CASCADE)
    upvotes = models.IntegerField(default=0)
    downvotes = models.IntegerField(default=0)
    score = models.IntegerField(default=0)
    date_created = models.DateField(default=timezone.now)
    parent = TreeForeignKey('self', on_delete=models.CASCADE,
                            null=True, blank=True, related_name='children')

    class MPTTMeta:
        order_insertion_by = ['-body']
        level_attr = 'mptt_level'

    def __str__(self):
        return self.body
