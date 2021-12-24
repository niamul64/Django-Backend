## image add ### media folder (we have to install pillow package for image or media input)
# must install pillow
$ pip install pillow     
$

### 1. in models.py: 
```
profile_pic= models.ImageField(upload_to='profile_pics', blank=True) # profile pic will be uploaded to 'media/profile_pics' folder
# we can add a default image: default='demo.png' # comming from media/demo.png
``` 
### 2.  model need to be registered in admin.py(see 'register model for admin panel.md')

1. Create a folder for media files, inside the main django project folder. 'media' and inside that foledr 'profile_pics'.
2. For best practice: make different different folder for differnt types of modules inside the media folder.
3. Now connect the media folder with the project: Goto settings.py ->
4. find the variable path of media folder. and add under the 'MEDIA_URL' :

### 3. Goto settings.py: (bottom of the settings.py)
```
MEDIA_DIR = os.path.join(BASE_DIR, 'media')
MEDIA_URL = '/media/'
MEDIA_ROOT = MEDIA_DIR

```
### 4. add media url to urls.py (must inport: settings, static, staticfiles_urlpatterns)
```
from django.conf import settings       
from django.conf.urls.static import static, staticfiles_urlpatterns

urlpatterns = [
      path....
]+static(settings.MEDIA_URL, document_root= settings.MEDIA_ROOT)   ## very important
```

### 5. Now in html file (very important [enctype="multipart/form-data"], [method="POST"] and [{% csrf_token %}])
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


### in views.py: if image file comming from html file and we are not using py forms:
```
  obj= Model() # a model with 'image' field 
  # here we have to check for POST request comming or not.
  if request.FILES.get('image'):    # if image comes
      obj.image = request.FILES['image']
      obj.save()
```
```
<!-- in HTML: -->
<input type="file" name="image" />
```