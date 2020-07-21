from django.shortcuts import render, reverse, HttpResponseRedirect
from subreddit.models import SubReddit,Moderator
from subreddit.forms import AddSubRedditForm
from authentication.models import RedditUser
from posts.models import Post
from subreddit.models import Moderator, FollowReddit
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
    if request.user.is_authenticated:
        moderators = Moderator.objects.filter(user=request.user)
        moderators = [moderator.user for moderator in moderators]
    else:
        moderators = None
    current_path = f'/r/{subreddit.name}/'
    return render(request, 'subreddit.html', {"subreddit": subreddit, "posts": posts, "current_path": current_path,"moderators": moderators})



def follow_subreddit(request, name):
    user = request.user
    subreddit = SubReddit.objects.get(name=name)

    if FollowReddit.objects.filter(user=user).filter(reddit=subreddit).exists():
        print("i exist")
        FollowReddit.objects.filter(user=user).filter(
            reddit=subreddit).delete()
        print("i was deleted")
    else:
        print("i do not exsist")
        FollowReddit.objects.create(
            user=user,
            reddit=subreddit
        )
        print("i am now created")

    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

def subredditnew(request, name):
    subreddit = SubReddit.objects.get(name=name)
    posts = Post.objects.filter(subreddit=subreddit.id).order_by("-date_created")
    if request.user.is_authenticated:
        moderators = Moderator.objects.filter(user=request.user)
        moderators = [moderator.user for moderator in moderators]
    else:
        moderators = None
    new_path = f'/r/{subreddit.name}/new/'
    return render(request, 'subreddit.html', {'posts': posts, 'subreddit': subreddit, "new_path": new_path,"moderators": moderators})


def subreddithot(request, name):
    subreddit = SubReddit.objects.get(name=name)
    posts = Post.objects.filter(subreddit=subreddit.id).order_by("-score")
    if request.user.is_authenticated:
        moderators = Moderator.objects.filter(user=request.user)
        moderators = [moderator.user for moderator in moderators]
    else:
        moderators = None
    hot_path = f'/r/{subreddit.name}/hot/'
    return render(request, 'subreddit.html', {'posts': posts, 'subreddit': subreddit, "hot_path": hot_path,"moderators": moderators})

