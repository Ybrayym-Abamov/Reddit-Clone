from django import forms
from django.contrib.auth.forms import UserCreationForm
from authentication.models import RedditUser


class LoginForm(forms.Form):
    username = forms.CharField(max_length=50)
    password = forms.CharField(widget=forms.PasswordInput)


class SignUpForm(UserCreationForm):
    class Meta:
        model = RedditUser
        fields = (
            'username',
            'email',
            'password1',
            'password2',
        )
