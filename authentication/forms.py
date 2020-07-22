from django import forms
from authentication.models import RedditUser


class LoginForm(forms.Form):
    username = forms.CharField(label='username', max_length=50, widget=forms.TextInput(
        attrs={'class': 'form-control'}), required=True)
    password = forms.CharField(label='password', max_length=50, widget=forms.PasswordInput(
        attrs={'class': 'form-control'}), required=True)


class SignUpForm(forms.Form):
    username = forms.CharField(label='username', max_length=50, widget=forms.TextInput(
        attrs={'class': 'form-control'}), required=True)
    password = forms.CharField(label='password', max_length=50, widget=forms.PasswordInput(
        attrs={'class': 'form-control'}), required=True)
    email = forms.EmailField(label='email', widget=forms.TextInput(
        attrs={'class': 'form-control'}), required=True)
