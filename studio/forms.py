from django.forms import ModelForm, ValidationError

from .models import Contact

from django import forms
from django.core import validators


# class ContactForm(forms.Form):
#     name = forms.CharField(max_length=100)
#     email = forms.EmailField()
#     subject = forms.CharField(max_length=256)
#     message = forms.CharField(widget=forms.Textarea)


class ContactForm(forms.ModelForm):
    
    class Meta:
        model = Contact
        fields = ('name', 'email', 'subject', 'message')