from django.urls import path
from posts.views import add_post, all_posts_view


urlpatterns = [
    path('addpost/', add_post, name='addpost'),
    path('allposts/', all_posts_view, name='allposts'),
]