from django.shortcuts import render, reverse, HttpResponseRedirect
from posts.models import Post
from posts.forms import AddPostForm
from authentication.models import RedditUser
from django.contrib.auth.decorators import login_required
from subreddit.models import SubReddit


# Create your views here.
def add_post(request):
    html = "addpost.html"

    if request.method == "POST":
        form = AddPostForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            Post.objects.create(
                title=data['title'],
                body=data['body'],
            )
            author = RedditUser.objects.get(id=request.user.id)
            # subreddit = SubReddit.objects.get(name=data['name'])
            post = Post.objects.get(title=data['title'])
            post.author.add(author)
            # post.subreddit.add(subreddit)
            post.save()
            return HttpResponseRedirect(reverse('homepage'))

    form = AddPostForm()

    return render(request, html, {"form": form})

@login_required
def up_vote(request, id):
    # http://www.cs.virginia.edu/~evans/cs1120-f09/ps/project/django.html
    up_post = Post.objects.get(id=id)
    up_post.upvotes += 1
    up_post.score += 1
    up_post.save()
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))



@login_required
def down_vote(request, id):
    down_post = Post.objects.get(id=id)
    down_post.downvotes += 1
    down_post.score -= 1
    down_post.save()
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


def postview(request,id,name):
    post = Post.objects.get(id=id)
    return render(request,'post.html',{'post':post})
