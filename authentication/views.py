from django.shortcuts import render, reverse, HttpResponseRedirect, redirect
from django.contrib.auth import logout, authenticate, login
from django.views import FormView
from authentication.forms import LoginForm
from django.contrib.auth.forms import UserCreationForm
from authentication.models import RedditUser

# Create your views here.
class LoginView(FormView):
    def get(self, request):
        form = LoginForm()
        return render(request, 'login.html', {'form': form})

    def post(self, request):
        form = LoginForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            user = authenticate(
                request,
                username = data['username'],
                password = data['password']
                )
            if user:
                login(request, user)
        return HttpResponseRedirect(reverse('homepage'))



class SignUpView(View):
    def get(self, request):
        return render(request, 'signup.html', { 'form': UserCreationForm() })

    def post(self, request):
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            return redirect(reverse('login'))

        return render(request, 'signup.html', { 'form': form })


def index(request):
    return render(request, 'main.html')