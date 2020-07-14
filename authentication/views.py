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
                request,
                username=data['username'],
                password=data['password']
                )
            if user:
                login(request, user)
        return redirect(self.request.GET.get('next'),reverse('homepage'))


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
                username = data['username'],
                email = data['email'],
            )
            new_user.save()
            login(request, new_user)
            return HttpResponseRedirect(reverse('login'))
        form = SignUpForm()
        return render(request, 'signup.html', {'form': form})


def index(request):
    posts = Post.objects.all()
    return render(request, 'subreddit.html', {'posts': posts})



class LogoutView(View):
    def get(self, request):
        logout(request)
        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))