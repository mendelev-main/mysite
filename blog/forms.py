from django import forms
from .models import Post, Tag


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = [
            "title",
            "body",
            "tag",
        ]


class TagForm(forms.ModelForm):
    class Meta:
        model = Tag
        fields = [
            "title",
        ]
