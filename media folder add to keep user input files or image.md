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


### in views.py: if image file comming from html file and we are not using py forms:
```
  obj= Model() # a model with 'image' field
  if request.FILES.get('image'):
      obj.image = request.FILES['image']
      obj.save()
```