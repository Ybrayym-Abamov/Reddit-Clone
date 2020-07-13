from django import forms
from posts.models import Post


class AddPostForm(forms.Form):
    title=forms.CharField(max_length=150)
    body=forms.CharField(widget=forms.Textarea)