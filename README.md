## Django-Backend
### What is django application:
Django Project is a collection of applications and configurations. Combining all applications will make our complete django website.
<br>
An application is created to perform a particular task like 1. registration, 2.posting blog, 3.comment etc.
<br>

### step1: Creating Django project (django-admin startproject [Name])
1. Create project folder and Create python env into it.(by pyhcharm-> easy). check python version from terminal($ python).
2. Install django.
$ pip install django==2.2
3. Create django project 'Practice_Project'
$ django-admin startproject Practice_Project

### step2: Running the server (python manage.py runserver)
1. Change directory to django project folder to run manage.py (for running the local server on port 8000). 
$ python manage.py runserver
2. Now if we want to change the port for running the server(lets say we want to run on port 7000)
$ python manage.py runserver 7000

### step3: Create APP (python manage.py startapp [App_name])
1. After Creating a django application, we allways have a main app.
2. Now, we can create other apps to perform a Particular task like 1. registration, 2.posting blog, 3.comment etc.
3. Create app 'first_app'.
$ python manage.py startapp first_app 
$
4. New app will be created beside the main app. And we need to connect that new app with project main app.
5. goto main app settings.py
6. And add a new instance in the 'NSTALLED_APPS' , the app name.

```
<settings.py folder>
INSTALLED_APPS = [
      .................    ,
    'first_app',
]
```

### step4: urls.py and views.py (url mapping is good practice)
##### always use this demo files for views and urls

```
# for urls.py:


from django.urls import path
from django.conf.urls import url # not for main app, only for extra created apps
from django.conf.urls import include # For Main urls.py only
from django.conf import settings
from django.conf.urls.static import static
from . import views ## for the own views import 
from [AppName] import views # for main app, import other app's views

urlpatterns = [
  path(.....),
]+static(settings.MEDIA_URL, document_root= settings.MEDIA_ROOT)


# for views.py import: 

from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from django.contrib import auth
from django.views.generic import ListView,detail
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.views.generic.edit import DeleteView
from django.contrib.auth import authenticate, login
from .models import ExtentionUser, PostAd
from .forms import UserReg, ExtentUser, PostAdForm
from django.core.mail import send_mail
import random
from django.conf import settings
import joblib
from predictor.models import Review,DataSet
```

1. --> web-browser--> request--> main_urls--> views--> response--> web-browser
2. From main urls.py for response we might goto the views.py, or othere apps urls.py  
3. For views: main app's views or other app's views (we need to import particular views to urls.py)
```
# import views.py inside the same app
-> import views
# import other App's views.py, in main app's urls.py
-> from [AppName] import views

# Now call views from urls.py (bad practice)
urlpatterns = [
    
    path('admin/', admin.site.urls),
    path('index/', views.index, name='index'), # forwarded to function based views named as 'index'. Do not need to specify app name as we importing the views.py(of all apps)
]
```

4. For main urls.py to other App's urls.py call (good practice)
```
#import this:
..........................#other imports
from django.conf.urls import include

# Add path:
urlpatterns = [
    path('', include('[AppName].urls')), # forwarded to [AppName].urls
    path('admin/', admin.site.urls), # admin path(default)
]
```

### step5: templates setup (show HTML files)
1. Create a folder inside the main django project folder. 'templates'
2. For best practice: inside the templates folder, we create a directory for each App.
3. Now, goto settings.py and TEMPLATES-> 'DIRS': ["templates"] <br>
BUT this is not good practice. it is like a hard coded path.

```
# good practice: goto settings.py and make a path for 'templates' folder (not hard coded)
TEMPLATES_DIR = os.path.join(BASE_DIR,'templates') ## here we will get the actual path for templates folder.
# now add the path to TEMPLATES-> 'DIRS': ["TEMPLATES_DIR"]
```

4. Now keep all HTML file in this templates folder. (use blocks in the html files)
5. Make a base HTML file and there declare many blocks, for other files. use those blocks.
by extending the base ({% extends 'base.html' %})
```
<!doctype html>
{% load static %}
<html lang="en">
  <head>

<link rel="stylesheet" href="{% static 'css/cssCode.css' %}"> <!-- css files links should be like this -->
  
  </head>
{% block block_name %}
.................
{% endblock%}
```
6. To render html file from views.
```
return render(request, 'path/fileName.html',{'objName1':ob1,'objName2':obj2,.......}) # path starts inside templates folder
```
### step6: static files in HTML files

1. Create a folder for static files, inside the main django project folder. 'static'
2. For best practice: make different different folder for differnt types of files inside the static folder.
3. Now connect the static file with the project: Goto settings.py ->
4. find the variable path of static file. and add under the 'STATIC_URL' :
```
# inside settings.py file
STATIC_DIR = os.path.join(BASE_DIR, 'static') # path of static folder
STATIC_URL = '/static/' # keep as it is. 
STATICFILES_DIRS= [
    STATIC_DIR, ## adding path 
]

```
5. Now to show the image from static/image folder, at .html file:
```
<!DOCTYPE html>

{% load static %}                                       <!-- Must include this tag -->

<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Index</title>
</head>

<body>
<h1>index page</h1>

<img src="{% static 'images/Capture.JPG' %}">            <!-- showing image -->

</body>
</html>
```

### step7: css, js or javaScript files in static files(see step 6 for static file setp-up)

1. Create a folder in static folder. 'css'
2. For best practice we should make folder for global css files and local css files(global-> used by all html files, local for each files)
3. Create a file for css code. 'cssCode.css' . add css code in this file.
4. Now, we need to use this css file for our index.html file. In the HTML file, inside the <head> tag:
```
# In the HTML file, inside the <head> tag
<link rel="stylesheet" href="{% static 'css/cssCode.css' %}">

```
5. In same way we can add JS files.

### step8: Built in models, Django Models, sqlLite3. Built in database.(This is not recommended for production level work)
1. We need django-models to work with db.sqlite3. SQL-Lite3 is a build in databsase with django.
2. In every app we have models.py file.
3. 'from django.db import models' this library should already been included in models. And this library contains all the classes and functions we need.

```
from django.db import models
from django.utils import timezone

class Musician(models.Model):
    id = models.AutoField(Primary_key=True)  # But we dont need this id field. its genarated by django automaticaly.
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)

    def __str__(self): #function to_string
        return self.first_name+" "+ self.last_name

class Album(models.Model):

    artist = models.ForeignKey(Musician, on_delete= models.CASCADE) # By using on on_delete: if Musician object deleted then coresponding album obj will also deleted
    name= models.CharField(max_length=100)
    release_date = models.DateField()
    num_stars =models.IntegerField()

    def __str__(self): #function to_string
        return self.name
```
4. Now we need to migrate the models. (allways run these 3 commands, when ever we change in models.py)
$ python manage.py migrate
$ python manage.py makemigrations [app_name: in which app we need to add models changes, if we do not give the app name, then it will do makemigrations to whole project ]
$ python manage.py migrate
$
5. Now, we have succesfully created database in sql-lite3.
6. Now, we can insert data from shell( step9), other wise we can insert data from admin panel: by creating superuser ( step10)

### step9: insert data in database from shell
1. from terminal use shell
$ python manage.py shell
$ # shell will open
```
# import models: (lets say our app name 'first_app' : with two models: 1.Musician 2. Album)
>>> from first_app import Musician, Album

#Now we can print the model all obj to see, is there any object in the model:
>>> print(Musician.objects.all) 

# Now to entry data, 
>>> obj =  Musician(first_name="Eric",last_name="H")
>>> obj.save()
# Now  if we print the values:
>>> print(Musician.objects.all) 
# we will see a obj
```
### ste10: insert data in database from admin panel 
1. Create a superuser:
$ python manage.py createsuperuser
$
2. goto admin.py file of the same App where the models are located.
```
# in admin.py file: (# import models: (lets say our app name 'first_app' : with two models: 1.Musician 2. Album))

from .models import Musician, Album

admin.site.register(Musician)
admin.site.register(Album)
```
3. Now run the server
$ python manage.py runserver
$
4. open admin panel and login as superuser. we will see the model where we can insert data.