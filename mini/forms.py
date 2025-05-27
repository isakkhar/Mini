from django import forms
from .models import Comment, ContactMessage

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
class ContactForm(forms.ModelForm):
    class Meta:
        model = ContactMessage
        fields = ['name', 'email', 'phone', 'subject', 'message']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control bg-gray-850 border-gray-800 color-gray-500', 'placeholder': 'Your name *'}),
            'email': forms.EmailInput(attrs={'class': 'form-control bg-gray-850 border-gray-800 color-gray-500', 'placeholder': 'Email *'}),
            'phone': forms.TextInput(attrs={'class': 'form-control bg-gray-850 border-gray-800 color-gray-500', 'placeholder': 'Phone number *'}),
            'subject': forms.TextInput(attrs={'class': 'form-control bg-gray-850 border-gray-800 color-gray-500', 'placeholder': 'Subject *'}),
            'message': forms.Textarea(attrs={'class': 'form-control bg-gray-850 border-gray-800 color-gray-500', 'rows': 5, 'placeholder': 'Message *'}),
        }