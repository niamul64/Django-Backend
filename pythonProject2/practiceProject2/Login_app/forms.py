from django import forms
from django.contrib.auth.models import User           # importing user model
from .models import UserInfo                          # UserInfo model import


class UserForm(forms.ModelForm):
    password= forms.CharField(widget= forms.PasswordInput())      # will help to make proper password field
    class Meta():
        model= User    # User model form
        fields = ('username', 'password', 'email' )               # not using other fields

class UserInfoForm(forms.ModelForm):
    class Meta():
        model= UserInfo                                           # UserInfo model
        fields = ('facebook_id', 'profile_pic')                   # not using User foreign key field

