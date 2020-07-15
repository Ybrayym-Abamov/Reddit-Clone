from django.shortcuts import render, reverse, HttpResponseRedirect
from posts.models import Post
from posts.forms import AddPostForm
from authentication.models import RedditUser
from django.contrib.auth.decorators import login_required
from subreddit.models import SubReddit
from comments.models import Comment
from comments.forms import AddCommentForm


# Create your views here.
def add_post(request, name):
    html = "addpost.html"

    if request.method == "POST":
        form = AddPostForm(request.POST)
        author = RedditUser.objects.get(id=request.user.id)
        subreddit = SubReddit.objects.get(name=name)
        if form.is_valid():
            data = form.cleaned_data
            Post.objects.create(
                title=data['title'],
                body=data['body'],
                author=author,
                subreddit=subreddit
            )
            post = Post.objects.get(title=data['title'])
            post.save()
            return HttpResponseRedirect(reverse('subreddit', kwargs={'name': name}))

    form = AddPostForm()

    return render(request, html, {"form": form})


@login_required
def up_vote(request, id):
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


def postview(request, id, name):
    post = Post.objects.get(id=id)
    comments = Comment.objects.filter(post=post)
    html = "addcomment.html"

    if request.method == "POST":
        form = AddCommentForm(request.POST)
        user = RedditUser.objects.get(id=request.user.id)
        post = Post.objects.get(id=id)
        if form.is_valid():
            data = form.cleaned_data
            Comment.objects.create(
                body=data['body'],
                user=user,
                post=post
            )
            comment = Comment.objects.get(body=data['body'])
            comment.save()
            return HttpResponseRedirect(reverse('postview', kwargs={'name': name, 'id': id}))

    form = AddCommentForm()
    return render(request, 'post.html', {'post': post, 'comments':comments, 'form':form})
