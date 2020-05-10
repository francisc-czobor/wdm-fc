from django import forms

from ..models.comment import Comment


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        exclude = ['created_at', 'post']
