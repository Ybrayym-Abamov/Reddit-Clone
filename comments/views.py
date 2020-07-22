from django.shortcuts import HttpResponseRedirect
from comments.models import Comment
from django.contrib.auth.decorators import login_required


# Create your views here.

@login_required
def up_vote(request, name, id, id2):
    # http://www.cs.virginia.edu/~evans/cs1120-f09/ps/project/django.html
    up_post = Comment.objects.get(id=id2)
    up_post.upvotes += 1
    up_post.score += 1
    up_post.save()
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


@login_required
def down_vote(request, name, id, id2):
    down_post = Comment.objects.get(id=id2)
    down_post.downvotes += 1
    down_post.score -= 1
    down_post.save()
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


def delete_view(request, id):
    comment = Comment.objects.get(id=id)
    comment.delete()
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
