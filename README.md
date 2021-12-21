### Django-Backend
### What is django application:
Django Project is a collection of applications and configurations. Combining all applications will make our complete django website.
<br>
An application is created to perform a particular task like 1. registration, 2.posting blog, 3.comment etc.
<br>

#### step1: Creating Django project (django-admin startproject [Name])
1. Create project folder and Create python env into it.(by pyhcharm-> easy). check python version from terminal($ python).
2. Install django.
$ pip install django==2.2
3. Create django project 'Practice_Project'
$ django-admin startproject Practice_Project

#### step2: Running the server (python manage.py runserver)
1. Change directory to django project folder to run manage.py (for running the local server on port 8000). 
$ python manage.py runserver
2. Now if we want to change the port for running the server(lets say we want to run on port 7000)
$ python manage.py runserver 7000

#### step3: Create APP (python manage.py startapp [App_name])
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

#### step4: urls.py and views.py (url mapping is good practice)
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