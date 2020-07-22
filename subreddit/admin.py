from django.contrib import admin
from subreddit.models import SubReddit, Moderator

# Register your models here.
admin.site.register(SubReddit)
admin.site.register(Moderator)
