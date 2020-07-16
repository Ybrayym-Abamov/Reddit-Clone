from django.urls import path
from posts.views import add_post, postview, up_vote, down_vote


urlpatterns = [
    path('r/<str:name>/addpost/', add_post, name='addpost'),
    path('r/<str:name>/post/<int:id>/', postview, name='postview'),
    path('upvote/<int:id>/', up_vote, name='upvote'),
    path('downvote/<int:id>/', down_vote, name='downvote')
]
