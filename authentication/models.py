from django.db import models
from django.contrib.auth.models import AbstractUser


class RedditUser(AbstractUser):
    karma = models.IntegerField(default=0)
    email = models.EmailField(max_length=150)
