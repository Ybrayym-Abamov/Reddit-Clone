from django.shortcuts import render, reverse, HttpResponseRedirect, redirect
from django.contrib import messages
from django.contrib.auth import logout, authenticate, login
from django.views import View
from authentication.forms import LoginForm, SignUpForm
from posts.models import Post
from django.contrib.auth.forms import UserCreationForm
from authentication.models import RedditUser
from subreddit.models import SubReddit


class LoginView(View):
    def get(self, request):
        form = LoginForm()
        return render(request, 'login.html', {'form': form})

    def post(self, request):
        form = LoginForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            user = authenticate(
                username=data['username'],
                password=data['password']
            )
            print(data)
            if user:
                login(request, user)
                return redirect(request.GET.get('next'), reverse('homepage'))
        return render(request, 'login.html', {'form': form})


class SignUpView(View):
    def get(self, request):
        form = SignUpForm()
        return render(request, 'signup.html', {'form': form})

    def post(self, request):
        form = SignUpForm(request.POST)
        if form.errors:
            messages.add_message(request, messages.INFO, 'Password invalid')
        if form.is_valid():
            data = form.cleaned_data
            new_user = RedditUser.objects.create_user(
                username=data['username'],
                email=data['email'],
                password=data['password']
            )
            new_user.save()
            login(request, new_user)
            return HttpResponseRedirect(reverse('homepage'))


def index(request):
    posts = Post.objects.all()
    subreddits = SubReddit.objects.all()
    sub_r_count = SubReddit.objects.all().count()
    subscribe_list = SubReddit.objects.filter(subscriber=request.user.id)
    return render(request, 'main.html', {'posts': posts, 'subreddits': subreddits, "sub_r_count": sub_r_count, "subscribe_list": subscribe_list})


def new(request):
    posts = Post.objects.all().order_by("-date_created")
    subreddits = SubReddit.objects.all()
    sub_r_count = SubReddit.objects.all().count()
    subscribe_list = SubReddit.objects.filter(subscriber=request.user.id)
    return render(request, 'main.html', {'posts': posts, 'subreddits': subreddits, "sub_r_count": sub_r_count, "subscribe_list": subscribe_list})


def hot(request):
    posts = Post.objects.all().order_by("-score")
    subreddits = SubReddit.objects.all()
    sub_r_count = SubReddit.objects.all().count()
    subscribe_list = SubReddit.objects.filter(subscriber=request.user.id)
    return render(request, 'main.html', {'posts': posts, 'subreddits': subreddits, "sub_r_count": sub_r_count, "subscribe_list": subscribe_list})


def following(request):
    following = FollowReddit.objects.filter(user=request.user)
    return render(request, 'main.html', {'posts': following})


class LogoutView(View):
    def get(self, request):
        logout(request)
        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
