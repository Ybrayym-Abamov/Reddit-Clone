from django.urls import path
from subreddit.views import add_subreddit


urlpatterns = [
    path('addsubreddit/', add_subreddit, name='addsubreddit'),
]