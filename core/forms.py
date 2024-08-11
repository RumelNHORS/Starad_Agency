# forms.py
from django import forms
from .models import ContactMessage


class ContactMessageForm(forms.ModelForm):
    class Meta:
        model = ContactMessage
        fields = ['name', 'email', 'message']
        widgets = {
            'message': forms.Textarea(attrs={'rows': 4, 'placeholder': 'Your Message *'}),
            'name': forms.TextInput(attrs={'placeholder': 'Enter your full name *'}),
            'email': forms.EmailInput(attrs={'placeholder': 'Enter your email *'}),
        }
