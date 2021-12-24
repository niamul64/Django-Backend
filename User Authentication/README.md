## For this readME.md: pythonProject2
## User Auth : djago provides a User Model (Needed field from this model is: username, password, email)
## We have app: main, Login_app

### step 1: relative URL: (good Practice) here i will use relative urls for all urls
### inside the app's (not main app): urls.py
```
from django.conf.urls import url
from django.urls import path
from . import views

app_name='Login_app'                     ###### for using relative URL insidt the HTML file:

urlpatterns = [
  path('', views.index, name='index'),
]

```
### Now, we can use ralative app Url: By mentioning the App_name:url_name:  inside the HTML file
```
href="{% url 'Login_app:index' %}"

<!-- to sent a obj id with it: -->
href="{% url 'Login_app:index' obj.id %}"
```

### step2: Create super user
$ py manage.py makemigrations
$ py manage.py migrate
$ py manage.py makemigrations
$ manage.py migrate
$ py manage.py createsuperuser
$
### step3: Models.py at Login_app
1. Import the User model
2. We will use username, email, password from this Model
3. To extend the information for User model we are creating another model which will be one_to_one relation-ship with User model
4. we will take profile image
5. so we need media folder. image add, media folder (see the 'media folder add to keep user input files or images.md' folder)
```
from django.db import models
from django.contrib.auth.models import User # Importing the User model for using authrization
                                            # We will use username, email, password from this Model

# Create your models here.
                                            # To extend the information for User model,
class UserInfo(models.Model):               # we are creating another model which will be one_to_one relation-ship with user model
    userID = models.OneToOneField(User, on_delete=models.CASCADE,primary_key=True) 
                                            # Connect user model with one_To_one relationship
                                            # and saying that, User model id willbe its ID
    facebook_id = models.URLField(blank=True)                                   # user can keep this field empty
    profile_pic= models.ImageField(upload_to='profile_pics', blank=True) # profile image will be uploaded to 'media/profile_pics' folder

    def __str__ (self):
        return self.user.username # accessing the user name from User model
```

### step4: Now, set the MEDIA folder for django project(see: "media folder add to keep user files or image.md").
### step5: register the model in admin.py (see: 'register model for admin panel')
1. follow step2.

<hr>

## Now we can add extra user info from admin panel: 
## Lets create a User registration system by forms.py

### Step1: forms.py (two models: User, UserOnfo) # User model is provided by django
```
# forms.py:

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
        model= UserInfo                               # UserInfo model
        fields = ('facebook_id', 'profile_pic')       # not using User foreign key field
```

### step2: make views for registration page, that will pass the forms to html and respose for user input
1. views.py:->import part:
```
from .forms import UserForm, UserInfoForm # importing 2 forms
from django.shortcuts import render
```
2. views.py:->views:
```
```  
3. urls.py:
```
path('register/', views.register, name='register'),

```

### step4: make a html file to show these 2 forms: 'register.html'
##### very important: [enctype="multipart/form-data"], [method="POST"] and [{% csrf_token %}]
```
{% extends 'Login_app/base.html' %}  # extending the base.html # here file path could be differernt
{% load static %}                    # static file load 
{% block head %} {% endblock %}

{% block body %}
<h3> Register </h3>

<!-- enctype="multipart/form-data"  and CSRF_token must be added for image/file data insert -->
<form action="" method="POST" enctype="multipart/form-data">
      {% csrf_token %}
      {{user.as_p}}
      {{userInfo.as_p}}
      <input type="submit" value="submit" name="submit">

</form>

{% endblock %}
```
