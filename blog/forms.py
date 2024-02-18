from django.forms import ModelForm
from django.contrib.auth.models import User
from django import forms
from . models import Blog, Comment

class BlogForm(forms.ModelForm):

    class Meta:
        model = Blog
        fields = '__all__'
        exclude = ['author', 'likes', 'status',]


class CommentForm(forms.ModelForm):

    class Meta:
        model = Comment
        fields = ('body',)
        labels = {
            'body': ''
        }
        widgets = {
            'body': forms.Textarea(attrs={'placeholder': 'Write a comment here', 'required': False}),
        }


class EditForm(forms.ModelForm):


    class Meta:
        model = Comment
        fields = ('body',)
        labels = {
            "body": "Make your changes below and click save",
        }