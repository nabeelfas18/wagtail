from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

# Sign Up Form
class ContactForm(UserCreationForm):
    name = forms.CharField(max_length=150, required=True, help_text='Please enter your name',widget=forms.TextInput(attrs={'class':'form-control','placeholde':'name'}))
    email = forms.EmailField(max_length=254,required=True, help_text='Enter a valid email address')
    subject = forms.CharField(max_length=250, required=True, help_text='Please enter the subject')
    message = forms.CharField(max_length=250, required=True, help_text='Please enter the message')

    class Meta:
        model = User
        fields = [
            'name', 
            'email', 
            'subject', 
            'message',  
            ]