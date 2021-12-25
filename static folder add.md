## static folder add in django project

1. Create a folder for static files, inside the main django project folder. 'static'
2. For best practice: make different different folder for differnt types of files inside the static folder.
3. Now connect the static folder with the project: Goto settings.py ->
4. find the variable path of static folder. and add under the 'STATIC_URL' :
```
# inside settings.py file. But this have changed for django 3 or above(see: 'initial setup for project,md file')
STATIC_DIR = os.path.join(BASE_DIR, 'static') # path of static folder
STATIC_URL = '/static/' # keep as it is. 
STATICFILES_DIRS= [
    STATIC_DIR, ## adding path 
]
# inside settings.py file. But this have changed for django 3 or above(see: 'initial setup for project,md file')
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