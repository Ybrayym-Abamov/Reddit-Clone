from django.urls import path
from subreddit.views import add_subreddit, subredditview



urlpatterns = [
    path('addsubreddit/', add_subreddit, name='addsubreddit'),
    path('r/<str:name>/', subredditview, name='subreddit')
]