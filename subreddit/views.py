from django.shortcuts import render, reverse, HttpResponseRedirect
from subreddit.models import SubReddit
from subreddit.forms import AddSubRedditForm
from authentication.models import RedditUser
from posts.models import Post
from subreddit.models import Moderator
from django.contrib.auth.decorators import login_required


@login_required
def add_subreddit(request):
    html = "addsubreddit.html"

    if request.method == "POST":
        form = AddSubRedditForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            SubReddit.objects.create(
                name=data['name'],
                description=data['description'],
            )
            Moderator.objects.get_or_create(
                user=request.user,
                is_moderator=True,
            )
            subscriber = RedditUser.objects.get(id=request.user.id)
            moderator = Moderator.objects.get(user=request.user)
            subreddit = SubReddit.objects.get(name=data['name'])
            subreddit.subscriber.add(subscriber)
            subreddit.moderator.add(moderator)
            subreddit.save()
        return HttpResponseRedirect(reverse('homepage'))

    form = AddSubRedditForm()

    return render(request, html, {"form": form})


def subredditview(request, name):
    subreddit = SubReddit.objects.get(name=name)
    posts = Post.objects.filter(subreddit=subreddit.id)
    current_path = f'/r/{subreddit.name}/'
    return render(request, 'subreddit.html', {"subreddit": subreddit, "posts": posts, "current_path": current_path})


def subredditnew(request, name):
    subreddit = SubReddit.objects.get(name=name)
    posts = Post.objects.filter(subreddit=subreddit.id).order_by("-date_created")
    new_path = f'/r/{subreddit.name}/new/'
    return render(request, 'subreddit.html', {'posts': posts, 'subreddit': subreddit, "new_path": new_path})


def subreddithot(request, name):
    subreddit = SubReddit.objects.get(name=name)
    posts = Post.objects.filter(subreddit=subreddit.id).order_by("-score")
    hot_path = f'/r/{subreddit.name}/hot/'
    return render(request, 'subreddit.html', {'posts': posts, 'subreddit': subreddit, "hot_path": hot_path})
