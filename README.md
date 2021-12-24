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
4. models have some other usefull parameters (see step11 )

```
from django.db import models
from django.utils import timezone

class Musician(models.Model): # models have some other usefull parameters (see step11 )
    id = models.AutoField(Primary_key=True)  # But we dont need this id field. its genarated by django automaticaly.
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    
    # when using MySql
    # class Meta: # by this , we can say to make the table with exactly this give name(force)
    #     db_table = "Musician" # table will be created by this name exactly.

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

### ste11: models have some other usefull parameters
#### by default all parameter value is false, but we can set those to true.
1. NULL, by default-> null= false, means value can not be null. But we can set it to True-> can set to be null.
2. BLANK, by default-> null= false, means value can not be blank. If you only set blank=True, then we can keep that fill blank
```
## default values:
columnName = models.CharField(max_length=120, default="" , null=False , blank= False)
## but we can:
columnName = models.CharField(max_length=120 null=True , blank= True) 

Example For img field:
img1 = models.ImageField(upload_to='images/post', default='demo.png',blank=True)
```

3. choices, Structure--> ('value for database', "value will show to user")
```
# we need to use tulpes data structure to keep the choices:
# example 1:(for charecter value)
    choice =(
            ('', 'Location'),
            ('Dhamrai', 'Dhamrai'),
            ('Dhanmondi', 'Dhanmondi'),
            ('Gulshan', 'Gulshan'),
            ('Jatrabari', 'Jatrabari'),
            ('Keraniganj', 'Keraniganj'),
            )
    location = models.CharField(max_length=120, null=False , blank= False, choices= choice)

# example 2 for integer value
    choice = (
        (None, 'rating'),
        (1, 'worst'),
        (2, 'bad'),
        (3, 'not good'),
        (4, 'good'),
        (5, 'excellent'),
    )
    num_stars =models.IntegerField(choices=choice)
    
    def __str__(self): #function to_string
        value,char= self.choice [self.num_stars]
        return self.name+ " "+ char
    
    def getRating(self): # Get the actuall String value from choices list
        value, char = self.choice[self.num_stars]
        return char
```
### ste12: Import models at views and values show to user through HTML page
#### ltes say we have two models in a App. APP name='first_app' , models= 'Musician', 'Album'
1. So, import:
```
from first_app.models import Musician, Album
```
2. in the views function, from where i will pass the model object to HTML:
```
# structure: variable= Model_name.objects.all().order_by('a column name') 

def index(request):
    musician_list = Musician.objects.all().order_by('first_name') # 'Musician' is the model name. 
    return render(request, 'first_app/index.html', {'mu_obj': musician_list,}) # it will pass the musician_list obj as 'mu_obj' to 'index.html' file. 
```
3. Now, from index.html file we can access the obj:
```
{% for obj in mu_obj %}   

{{obj.first_name}}
{{obj.last_name}}

{% endfor %}

```

### ste13: Form with HTML

#### must use '{% csrf_token %}' in the form tag
#### must use enctype="multipart/form-data" in starting form tag.(for image or file data insert)
#### ltes say we have two models in a App. APP name='first_app' , models= 'Musician', 'Album'
1. create a form in html. Here two types of methods are here: post, get 
2. both 2 methods (post and get) passes the information, one page to another. (get: visible info(for search). post: invisible info (for insert value in database))
3. There is an action ="" field where we will mention where to go if successfully submited the form.
4. required, if we use required then we can not submit the form without filling that field

```
## note: here for = "Same" and name= "Same". and we all so grab the value at views, of input tag by name = ""

    <form class="" action="{% url 'index' %}" method="post" enctype="multipart/form-data">   
        {% csrf_token %} <!-- # must use.  -->

    <!-- ## note: action field: where we will mention where to go if successfully submited the form-->
    
    <!-- ## note: here for = "Same" and name= "Same".-->
        <label for="first_name">Insert Your Name</label>
        <input type="text" name="first_name" value= "initial value" placeholder="blur message" required> 
    <!--note:(backend relation) We grab the value at views, of input tag by name = ""-->

    <input type="submit" name= "submit" value="Submit">

    </form>
```
5. Now, from views.py--> function
```
  obj = Mucician() # create a object of database table
  if request.method == 'POST':
      f_n = request.POST['first_name']
      obj.first_name=f_n
      obj.save()
```
6. If we have image file: views.py--> function
```
  obj = Mucician()  # create a object of database table
  if request.FILES.get('image'):
      obj.image = request.FILES['image']
      obj.save()
```

### ste14: form.py ( {{pyform.as_p}}, {{pyform.as_table}}, {{pyform.as_ul}} ) (see step20 for many kinds of fields of forms.py)
#### forms has many fields: CharField, EmailField, IntegerField, URLField, etc.
#### ltes say we have two models in a App. APP name='first_app' , models= 'Musician', 'Album'
1. Make a file in the App directory of 'first_app' called 'forms.py'
2. Now, inside forms.py file, import:
```
from django import forms
```
3. Now, every form is a class. there are many arguments that we can use in the bracket of form
visit the link to see all these arguments: https://docs.djangoproject.com/en/4.0/ref/forms/fields/ . Now, django form do not provide some arguments, like we use 'placeholder' in HTML. (See step15)
```
class Mucician(forms.Form):
    first_name= forms.CharField(lable='First Name', required=True, initial="Niamul", )
    last_name= forms.CharField(error_messages={'required': 'Please enter your name'})
    Email = forms.EmailField(required=False,)      # example of required arguments 
```
4. we can import this form inside views.py
```
from first_app import forms # will import all froms from forms.py file
```
5. Now inside the function of views.py, we can create a obj of the form and pass to html.
```
  pyForm= forms.Mucician() # here, Mucician is the form name. (forms is the forms.py file)
  return render(request, 'first_app/form.html', {'pyform':pyForm, })
```
6. Now, at html file we can access and show the form:
#### must use '{% csrf_token %}' in the form tag.
#### must use enctype="multipart/form-data" in starting form tag.(for image or file data insert)
```
<!--HTML file-->
<form class="" action='{% url "index" %}' method="post" enctype="multipart/form-data"> 
    {% csrf_token %} 

    {{pyform}}  <!-- showing form we also can use: {{pyform.as_p}} -->

                <!-- in {{pyform.as_p}} , as_p= show as paragraph, means all lebel and input in new line -->
                <!-- in {{pyform.as_table}} , as_p= show as table -->
                <!-- in {{pyform.as_ul}} , as_p= show as unorder list -->
    
    <input type="submit" name= "submit" value="Submit">
</form>
```

### ste15: Widget, Arguments of form. There are many arguments that we can use in the bracket of form
visit the link to see all these arguments: https://docs.djangoproject.com/en/4.0/ref/forms/fields/ . 
#### Now, django form do not provide some arguments, like we use 'placeholder' in HTML. (by using widget we can use these argumentes)
1. Now, lets use widget--> widget is a argument, in this argument we can send html atributs.
2. Structure: (widget =forms.TextInput(attrs={ 'placeholder': "Enter your first name " })) # Here attrs = Attributs, we need to send the Attributs in a form of dictionary in the 'attrs'.
3. by this we can pass all the atributs that html has. we all so can pass css attributs by this
```
class Mucician(forms.Form):
    first_name= forms.CharField(label='First Name',  widget =forms.TextInput(attrs={'placeholder': "Enter your first name ", 'style':'width:300px; height:400px;'}) )

    last_name= forms.CharField(error_messages={'required': 'Please enter your name'})
    Email = forms.EmailField(required=False,)      # Example of required arguments 
    
    # for HTML part, see step13 -->4
``` 

### ste16: DATE OF BIRTH field in forms.py using calender.
```
    #inside the forms.py file--> inside the class:
    date_of_birth=forms.DateField(widget= forms.TextInput(attrs={
        'type':'date',
    }))
    # for HTML part, see step14
```

### step17: form submit ( for html form: see step13 || Py forms see this step )
#### must use '{% csrf_token %}' in the form tag.
#### must use enctype="multipart/form-data" in starting form tag.(for image or file data insert)
1. the form at forms.py file --> see step step15 and 16
```
# forms.py
class Mucician(forms.Form):
    first_name= forms.CharField(label='First Name',  widget =forms.TextInput(attrs={'placeholder': "Enter your first name ", 'style':'width:300px; height:400px;'}) )
    last_name= forms.CharField(error_messages={'required': 'Please enter your name'})
    Email = forms.EmailField(required=False,)      # Example of required arguments 
        date_of_birth=forms.DateField(widget= forms.TextInput(attrs={
        'type':'date',
    }))
    # for HTML part, see step14
```
2. and html at step 13
3. Now, submit form and grab the value at views.py file and check the inserted values are valid or not: (this form is pyForm)

```
def form(request):
    pyForm= forms.Mucician()                                     # Here, Mucician is the form name. (forms is the forms.py file)
    diction={}

    if request.method == "POST": # if any post request
        submitedForm= forms.Mucician(request.POST)               # grab the submitted form

        if submitedForm.is_valid():                              # form validation check
            first_name= submitedForm.cleaned_data['first_name']  # grabing each values
            last_name= submitedForm.cleaned_data['last_name']
            email= submitedForm.cleaned_data['email']
            date_of_birth= submitedForm.cleaned_data['date_of_birth']

            #just pass the values at html page, to show.
            diction.update({'first':first_name})                  # thats how we can concatenate with previous dictionary
            diction['last'] = last_name                           # thats how we can concatenate with previous dictionary
            diction.update({'email': email})
            diction.update({'dob': date_of_birth})
            diction.update({'form_sub_check': 'yes'})             # for checking at the html page
            pyForm= submitedForm
    
    diction['pyform']= pyForm
    return render(request, 'first_app/form.html', context=diction)
```

### step18: Custom form validation || submited py form save into database 
1. See previous step for, how we can grab value at views.py for a pyFrom.
2. Now, import to forms.py file (from django.core import validators)
```
## built in validator:
from django import forms
from django.core import validators
class Validator(forms.Form):
    name_field= forms.CharField(validators=[validators.MaxLengthValidator(20), validators.MinLengthValidator(10)])
    number_field=forms.IntegerField(validators=[validators.MaxValueValidator(15),validators.MinValueValidator(5)])
```
3. custom validators:
```
def even_number_check(value): # 'value' will receive the value from the field
    if value % 2 == 1:
        raise forms.ValidationError("Please Insert an Even Number") # pass this error message

class Validator(forms.Form):
    number_even= forms.IntegerField(validators=[even_number_check]) # from here passing the value to 'even_number_check(value)'
```
4. custom validators: for email match Check
```
class Email_match_Check(forms.Form):
    email = forms.EmailField()
    email_varification = forms.EmailField()

    def clean(self):
        all_cleaned_data= super().clean()            # Now this super() will take all the values of fields and store to the 'all_cleaned_data' variable
                                                     #all_cleaned_data grabs the value of to email fields.
        email1= all_cleaned_data['email']
        email2= all_cleaned_data['email_varification']

        if email1 != email2:
            raise forms.ValidationError("Fields are not matched!") # error message pass
```

## step19: save(), save into model using py form or forms.py, ModelForm
#### After validating and checking we need to save the information into database
1. At first we need to import model classes at forms.py file
```
from first_app.models import Musician
```
2. Now, for model form we need to extend ModelForm from forms, 'forms.Form' will not work here
```
class MusicianForm(forms.ModelForm):
```
3. Now, we need to use a Meta class for model form: Meta class means class inside a class:
4. Now, inside the Meta class we need to specify, which model class we are using to make form
5. Now, we need to specify, wchih field we are keeping for form. (if we keep all fields then: fields="__all_")
```
# inside forms.py file-->

from django.core import validators
from first_app.models import Musician
class MusicianForm(forms.ModelForm):
    class Meta:
        model= Musician
        fields="__all__"        #    For all fields
        # exclude=['first_name']  #    by excludein we can ingnore the first_name field
        # fields = ('username', 'email', 'password1', 'password2' ) # only mentioned field will be displayed
```
6. Saving to database:
```
# inside views.py file-->

def form(request):
    pyForm= forms.MusicianForm()          # here, MucicianForm is the form name. (forms is the forms.py file)
    diction={}
    if request.method == "POST":                                  # if any post request comes
        submitedForm= forms.MusicianForm(request.POST)            # grab the submitted form
        pyForm = submitedForm

        if submitedForm.is_valid():                               # form validation check
            submitedForm.save(commit=True)                        # Saving to database
            return index(request)                                 # sending request to another view

    diction['pyform']= pyForm
    return render(request, 'first_app/form.html', context=diction)
```
7. we can pass the user request to another view:
```
def form(request):
    return index(request) # sending form views to index view
```


### step20: Many fields for forms.py
1. see this link to have idea about the fields: https://docs.djangoproject.com/en/4.0/ref/forms/fields/
2. here in the doc we will notice the 'Default widget' to have idea about how the field looks or be handeled.
```
class User_form(forms.Form):
    boolean_field = forms.BooleanField(required=False)          # its a check box input
    char_field=forms.CharField(max_length=20,min_length=5)

    # sturcture of tuple--> ('value for database', 'value to show user')
    choice = (
        (None, 'rating'),
        (1, 'worst'),
        (2, 'bad'),
        (3, 'not good'),
        (4, 'good'),
        (5, 'excellent'),
    )
    choice_field= forms.ChoiceField(choices=choice)
    redio_button=forms.ChoiceField(choices=choice, widget= forms.RadioSelect) # by 'RadioSelect' built in widget we can make it redio button
    Multiple_Choice=forms.MultipleChoiceField(choices=choice, widget=forms.CheckboxSelectMultiple)   # values will come as a list ['1', '2']
```

### step21: Template filter for HTML files: see the link: https://docs.djangoproject.com/en/4.0/ref/templates/
#### see the filter option.
```
{{ text | upper }} <!--will make all charecter upper case-->
{{ text | lower }} <!--will make all charecter lower case-->
{{ number | add: '4' }} <!--if we are passing a number+4 = ? math addition will happen -->
{{ text | cut: "t" }} <!--if text='atvtsftgetr' then output will be: 'avsfger'-->

{{ text | cut: "t" | upper }} <!--multi filter-->

{{date_value| date: "D, d M Y"}} <!--date time, best: see documentation-->
```
### step22: custom filters for templates
1. first we need to add a folder inside the first_app folder(inside app folder for which's template we are modifying): 'templatetags'
2. Now, create a 2 python file inside the 'templatetags' folder. One file name could be anything but 'my_filters.py' prefarable. and another file name must be '__init__.py'. by crating '__init__.py' file django will consider this file as library file.

3. import:-> inside the my_filters.py file (from django import template):
```
from django import template
register= template.Library() #these two lines are fixed 
```
4. filter creating inside the: my_filters.py
```
from django import template
register= template.Library()

# Now filters are written as function
def my_filter(value):                     # this is custom filter. here 'value' accept the value from HTML carly tag {{ text }}
                                          # now Lets say our filter will add a string with received string
    return value +" this is string from custom filte"

# now register the function as filter
register.filter("custom_filter", my_filter) # now if we call "custom_filter" then 'my_filter' function will work
```
5. We need to load the filter inside html file where we want to use that filter: (under the {% extends 'base.html' %} we will included: {% load my_filters %})
```
{% extends 'base.html' %}
{% load my_filters %}                       <!--# loding the filter file, very important-->

<p>First Name:{{text | custom_filter}}</p> <!--from here 'text' will be sent to custom_filter-->

```
6. After doing all the things we need to re-start our server.

7. if we want, our filter accept a value.
```
{% extends 'base.html' %}
{% load my_filters %}                       <!--# loding the filter file, very important-->

{{text | custom_filter: 'abc' }} <!-- we want to pass a parameter from html to custom filter-->
```
8. Now, make changes at my_filter.py:
```
from django import template
register= template.Library()

# Now filters are written as function
def my_filter(value, filter_parameter):   # this is custom filter. here 'value' accept the value from HTML carly tag {{ }}
                                          # now Lets say our filter will add a string with received string
    return value +" "+ filter_parameter

# now register the function as filter
register.filter("custom_filter", my_filter) # now if we call "custom_filter" then 'my_filter' function will work
``` 

### step23: coonect Mysql database: see the video in this reposetory, name: connecting MySql Database.
---> from here see the folder 'WITH MySql Database'
