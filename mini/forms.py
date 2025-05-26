from django import forms
from .models import Comment

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('name', 'email', 'body')
        widgets = {
            'body': forms.Textarea(attrs={
                'class': 'form-control bg-gray-850 border-gray-800 bdrd16 color-gray-500 p-3',  # p-3 adds padding
                'rows': 5,
                'placeholder': 'Write a comment'
            }),
            'name': forms.TextInput(attrs={
                'class': 'form-control bg-gray-850 border-gray-800 bdrd16 color-gray-500 p-3',  # p-3 adds padding
                'placeholder': 'Your Name'
            }),
            'email': forms.EmailInput(attrs={
                'class': 'form-control bg-gray-850 border-gray-800 bdrd16 color-gray-500 p-3',  # p-3 adds padding
                'placeholder': 'Your Email'
            }),
        }