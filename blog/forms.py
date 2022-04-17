from pyexpat import model
from tkinter import Label
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm,UsernameField
from django import forms
from django.contrib.auth.models import User
from django.utils.translation import gettext,gettext_lazy as _
from . models import Post

class SignUpForm(UserCreationForm):
    password2=forms.CharField(label="Confirm Password(again)",widget=forms.PasswordInput(attrs={'class':'form-control'}))
    password1=forms.CharField(label="Password",widget=forms.PasswordInput(attrs={'class':'form-control'}))
    class Meta:
        model = User
        fields = ['username','first_name','last_name','email']
        labels ={'first_name':'First Name','last_name':'Last Name','email':'Email'}
        widgets ={'username':forms.TextInput(attrs={'class':'form-control'}),
                  'first_name':forms.TextInput(attrs={'class':'form-control'}),
                  'last_name':forms.TextInput(attrs={'class':'form-control'}),
                  'email':forms.EmailInput(attrs={'class':'form-control'}),
                  }
        
class LoginForm(AuthenticationForm):  
    password=forms.CharField(widget=forms.PasswordInput(attrs={'autofocus':True,'class':'form-control'}))
    username=UsernameField(widget=forms.TextInput(attrs={'autocomplete':'current-password','class':'form-control'}))
    
    
class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title','desc']
        labels = {'title':'Title','desc':'Description'}
        widgets = {'title':forms.TimeInput(attrs={'class':'form-control'}),
                   'desc':forms.Textarea(attrs={'class':'form-control'}),}
        
        
   
