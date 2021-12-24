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
## Lets create a User registration system

### Step1:

