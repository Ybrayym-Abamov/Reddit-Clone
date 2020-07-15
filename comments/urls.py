from django.urls import path
from comments.views import up_vote, down_vote


urlpatterns = [
    path('r/<str:name>/post/<int:id>/upvote/<int:id2>/', up_vote, name='comment_upvote'),
    path('r/<str:name>/post/<int:id>/downvote/<int:id2>/', down_vote, name='comment_downvote')
]
