from django import forms
from subreddit.models import SubReddit


class AddSubRedditForm(forms.ModelForm):
    class Meta:
        model = SubReddit
        fields = [
            'name',
            'description',
        ]