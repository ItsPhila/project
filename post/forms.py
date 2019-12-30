from django import forms
from .models import Comment, Post
class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        exclude = ['post','pubdate']
class AddPost(forms.ModelForm):
    class Meta:
        model = Post
        exclude = ['author']