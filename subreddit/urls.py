from django.urls import path
from subreddit.views import add_subreddit, subredditview, subreddithot, subredditnew


urlpatterns = [
    path('addsubreddit/', add_subreddit, name='addsubreddit'),
    path('r/<str:name>/', subredditview, name='subreddit'),
    path('r/<str:name>/new/', subredditnew, name='subredditnew'),
    path('r/<str:name>/hot/', subreddithot, name='subreddithot')
]
