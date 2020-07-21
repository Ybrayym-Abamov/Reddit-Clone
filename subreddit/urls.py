from django.urls import path
from subreddit.views import add_subreddit, subredditview, follow_subreddit


urlpatterns = [
    path('addsubreddit/', add_subreddit, name='addsubreddit'),
    path('r/<str:name>/', subredditview, name='subreddit'),
    path('follow/<str:name>/', follow_subreddit, name='follow'),
]
