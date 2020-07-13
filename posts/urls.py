from django.urls import path
from posts.views import add_post


urlpatterns = [
    path('addpost/', add_post, name='addpost')
]