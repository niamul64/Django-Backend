### 1. first create virtual environment 'env1' (see: 'virtual env.md')
### 2. Now install django==3.2.8
### 3. install packages for rest framework (see: 'rest framework.md')
### 4. Now create a django project
### 5. create django project ( django-admin startproject [project_name]): django-admin startproject MyApi
### 6. Now, enter inside the django project file. and start a app (py manage.py startapp [app_name]):py manage.py startapp status
### 7. create 3 directories named 'media', 'static' and 'templates', under the django project directory. 
### 8. goto settings.py--> 

```
INSTALLED_APPS = [
    .............other default paths,
	'App_name',
	'App_name',
	.......include all the app names that created,

	'rest_framework', # if we are using this
	'crispy_forms',   # if we are using this #pip install django-crispy-forms
	
]

### this is for django 3.2 or above for 2.2 or below see README.md of this directory
### Build paths inside the project like this: BASE_DIR / 'subdir'. # this is how we will find path for other folder

### BASE_DIR = Path(__file__).resolve().parent.parent   # given base dir
### Now, for static,media and templates: 

TEMPLATES_DIR= BASE_DIR /  'templates' ##########
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [TEMPLATES_DIR,],
##..............................


# Come to bottom of the page

STATIC_DIR= BASE_DIR /  'static' ###############
STATIC_URL = '/static/'
STATICFILES_DIRS = [
    STATIC_DIR,
]

MEDIA_DIR=  BASE_DIR / 'media'   ################
MEDIA_ROOT= MEDIA_DIR
MEDIA_URL = '/media/'



LOGIN_REDIRECT_URL = " "  ## in Loing error auto take url
```

### 9. Create database model classes,  see: 'django model.md'.
### 10. register models in admin panel: (run migrate, makemigrations--> before this)
### 11. createsuperuser (py manage.py createsuperuser)
### 12. create admin panel serialization on admin panel( see: 'admin panel serializer.md')  (optional)