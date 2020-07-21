from django import forms
from comments.models import Comment


class AddCommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = [
            'body',
        ]
        widgets = {'body': forms.Textarea(attrs={'rows':4, 'cols':80})}
