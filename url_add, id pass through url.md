## pass id through url
```
href="{% url 'url_name' %}"
Example: 

#for urls Path inside the main app:
--> need to import: from django.conf.urls import include
--> path('', include('first_app.urls')),# it will be forwarded to first_app's urls.py file

#For urls Path(not inside the main app, app: first_app): 
--> path('album_form/', views.album_form, name='album_form')

# Now, at html files


# url: 
href="{% url 'album_form' %}"

# To pass id: url: 

href="{% url 'album_form' obj.id %}"
# or 
href="{% url 'album_form' id %}"
```
## receive id at urls.py
Structure:    path('album_form/<int:variable_that_receive_id>/', views.album_form, name='album_form'),
```
 path('album_list/<int:artist_id>/', views.album_form, name='album_list'),

 # this id will pass to album_list views.
```

## views.py 
```           
def album_list(req, artist_id):                              # by artist_id variable we are receiving the value of id
    # here if we need the we can get the musician info
    # artist= Musician.objects.get( id=artist_id )
    # or
    # details = get_object_or_404(Musician, id= artist_id) # but for htis we need a library to import
    # (from django.shortcuts import get_object_or_404)

    albums_of_MU = Album.objects.filter(artist= artist_id)   # using foreign key value mathcing for filter

    diction={'title': "List of Album", "album":albums_of_MU,'artist': albums_of_MU[0].artist } #passing artist through foreignKey
    return render(req, 'first_app/album_list.html', context=diction)
```
## To html: we can go through the foreign key value and find the parent table values:
```
<ul>
      {% if album %}
      <li>
            Name of artist: {{artist.first_name}} <span> </span> {{artist.last_name}} 
      </li>
      {% for obj in album %}

      <li>
            Music Name: {{obj.name}}
      </li>
      <li>
            Relese Date: <span> </span> {{obj.release_date|date:"M d, Y" }} <!--with time date formate weidget-->
      </li>
      <li>
            Ratings: <span> </span> {{obj.num_stars}}
      </li>
      {% endfor %}
      {% endif %}
</ul>
```


# relative URL: (good Practice)

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
### Now, we can use ralative app Url: By mentioning the App_name:url_name: inside the HTML file
```
href="{% url 'Login_app:index' %}"

<!-- to sent a obj id with it: -->
href="{% url 'Login_app:index' obj.id %}"
```

