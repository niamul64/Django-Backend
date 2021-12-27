### clean image file in the image data is deleted or updated

### solution is using a package: (make sure--> we are at the vertual env)
$ pip install django_cleanup
$

# Now, we need to add it in the settings.py--> INSTALLED_APPS:
```
INSTALLED_APPS = [
      ............. ,
    'django_cleanup',
    .............   ,
]
```