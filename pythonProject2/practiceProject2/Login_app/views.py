from django.shortcuts import render
from .forms import UserForm, UserInfoForm

# Create your views here.

def index(req):
    dict={'Title': 'Index Page',}

    return render(req, 'Login_app/index.html', context=dict)

def register(req):
    dict={'Title': 'Register',}
    user= UserForm()        # UserForm Object
    userInfo=UserInfoForm() # UserInfoForm Object




    dict['user']=user
    dict['userInfo']=userInfo
    return render(req, 'Login_app/register.html', context=dict)