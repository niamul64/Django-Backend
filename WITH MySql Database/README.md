## connect MySql database. coonect Mysql database: see the video in this reposetory, name: connecting MySql Database.
Now we need to migrate the models. (allways run these 3 commands, when ever we change in models.py)
$ python manage.py migrate
$ python manage.py makemigrations [app_name: in which app we need to add models changes, if we do not give the app name, then it will do makemigrations to whole project ]
$ python manage.py migrate
$

## Make crud APP  with MySql database. 
<br>

### Re-name database, table name.
1. We can use metaclass inside model-classes to re-name the database table name.
2. Creating mySql database tables are same as we created for sqlite3 through Modelviews(ORM:object relation mapping)
### See Main README.md-- step8


## lets say we have two models Musician, Album in models.py file
```
# lets say we have two models Musician, Album in models.py file
class Musician(models.Model):
    #id = models.AutoField(Primary_key=True)  # But we dont need this id field. its genarated by django automaticaly.
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)

    # when using MySql (not recommended)
    # class Meta: # by this , we can say to make the table with exactly this give name(force)
    #     db_table = "Musician" # table will be created by this name exactly.

    def __str__(self): #function to_string
        return self.first_name+" "+ self.last_name

class Album(models.Model):
    # id = models.AutoField(Primary_key=True)  # But we dont need this id field. its genarated by django automaticaly.
    artist = models.ForeignKey(Musician, on_delete= models.CASCADE) # By using on on_delete: if Musician object deleted then coresponding album obj will also deleted
    name= models.CharField(max_length=100)
    release_date = models.DateField()
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
```



## first C= create. ADD values to database

### step1: forms.py , model form, field over write.
```
from django import forms
from django.core import validators
from first_app.models import Musician, Album

class MusicianForm(forms.ModelForm):
    class Meta:
        model= Musician
        fields = "__all__"  #    For all fields

class AlbumForm(forms.ModelForm):
    # Now over write the release_date field from 'Album' table

    release_date= forms.DateField(widget= forms.TextInput(attrs={'type':'date',})) # it will bring a callender in frontend
    class Meta:
        model= Album
        fields = "__all__"  #    For all fields
```
### step2: views.py 
```
from first_app.forms import MusicianForm

def musician_form(req):
    form= MusicianForm()                # creating object of MusicianForm
    
    if req.method == 'POST':            # if form submited
        form = MusicianForm(req.POST)   # grabing the form
        if form.is_valid():             # checking form is valid or not
            form.save(commit=True)      # saving to the database
            return homePage(req)        # if form saved the we will redirect to home page

    diction={'title': 'Add Musician', 'musician_form': form}
    return render(req, 'first_app/musician_form.html', context=diction)

def album_form(req):
    form = AlbumForm()                  # creating object of AlbumForm

    if req.method == 'POST':            # if form submited
        form = AlbumForm(req.POST)      # grabing the form

        if form.is_valid():             # checking form is valid or not
            form.save(commit=True)      # saving to the database
            return homePage(req)        # if form saved the we will redirect to home page

    diction= {'title': 'Add Album', 'album_form':form}
    return render(req, 'first_app/album_form.html', context=diction)
```
### step3: musician_form.html
```
<!-- here: {% csrf_token %} , method="POST" and enctype="multipart/form-data"  very important -->
<form class="" action="" method="POST" enctype="multipart/form-data"> 
    {% csrf_token %}
      {{musician_form.as_p}}
      <input class="btn btn-primary btn-sm" type="submit" name="submit" value="submit">
</form>
```

## Now R= read. READ values from Database and show it to HTML. to home.html or homePage

### But here, read from database is for two tables. where Album table has a foreign key--> Musician
### We will read the records from database for --> Musiciantable and show to homePage
### if any one clicks to any musician name, then it will show the albums of that particular musician's
### we will query by froeigen key to show the albums of musician
### we will see album info at album_list,html page.

### step1: at views.py
```
def homePage(req):                                         # Showing  records of Musicians
    read = Musician.objects.all().order_by('first_name')   # grab all the records from database of Musician table,using ORDER by
    diction = {'title': "Home Page", 'musician_list': read}# passing all the records to html page
    return render(req, 'first_app/home.html', context=diction)
```

### step2: at home.html
```
<h3> Home Page </h3>
<h5> List of Musicians: </h5>
<ul>
      {% if musician_list %}
      {% for obj in musician_list %}
      <li>

      <!-- Here, showing  the musician's name as link which will redirect to album_list page with the id of musician-->
           <a href="{% url 'album_list' obj.id %}"> {{obj.first_name}} <span> </span> {{obj.last_name}}</a>

      </li>
      {% endfor %}
      {% endif %}
</ul>
```

### step3: Passed if from homePage have to be receied at urls.py
```
 path('album_list/<int:artist_id>/', views.album_form, name='album_list'), #this id will pass to album_list views.
```
### step4: views.py will receive the id
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
### step4: Now at HTML file to show the info of album
```
<h3>Album List:</h3>
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
            Relese Date: <span> </span> {{obj.release_date|date:"M d, Y" }}  <!--with time date formate weidget-->
      </li>
      <li>
            Ratings: <span> </span> {{obj.num_stars}}
      </li>
      {% endfor %}
      {% endif %}
</ul>
```


## Now U = update: edit the information
## we will add edit button to album_list page and by cliking that user will able to edit information of a album
## but it is almost like create or save data in database database 

### step1: start form HTML page where we have album list and add a edit button for each album info
1. make a new html file where we will be redirected to edit the info, after clicking the edit button.

``` 
<!-- inside the HTML file where list are showing:  add a edit button for each album, inside the for_loop-->
     
      <a href="{% url 'edit_album' obj.id %}" class="btn btn-warning btn-sm">Edit</a>
      <!-- sending id of a album, to edit_album url, Now we need to receive the is form that url -->
```
### step2: get the id At urls.py
```
path('edit_album/<int:album_id>/', views.edit_album, name='edit_album'), #<int:album_id> is use to grab the id and pass to views
```
### step3: views, recieve the album_id with request:
```
def edit_album(req, album_id):
    dict={'title': 'Edit Album'}

    album= get_object_or_404(Album, id=album_id) # geting the particular album, by album id
    # Here we also could use
    # album= Album.objects.get(id=album_id) # same

    form= AlbumForm( instance = album)      # form obj with previously filled value, 'instance=album' gives the previous value

    if req.method=='POST':

        form = AlbumForm(req.POST, instance= album) # Grab the new filled info into previously filled form obj
    
        if form.is_valid:             # checking the input is valid or not
            form.save(commit=True)    # saving to database, exactly in the previously filled obj
    
            dict['success']="updated" # if successfully updated the value, passing a message

    dict["form"]=form
    dict['album_id']= album_id # needed, when we will delete the album.
    return render(req, 'first_app/edit_album.html', context=dict )     
```

### step4: Now, at the edit_album.html we will see the form with previously filled values and we can edit and submit
```
{% if success %} # if success msg comes
<hr>
{{success}}
<hr>
{% endif%}

<form class="" action="" method="POST">
    {% csrf_token %}
      {{form.as_p}}
      <input class="btn btn-primary btn-sm" type="submit" name="submit" value="submit">
</form>
```

## Now, D = delete records, delete data from database

1. In edit_album html page, add a delete button with <a> and add a onclik JS code to pop up a window to have a confirmation.
2. Then if confirms then send the album_id to url and by url--> pass it to views.
3. The url link is to redirect to a page where, successfull message will show --> delete_album.html

### step1: Inside edit_album.html, add delete button with onclick, pass album_id  
```
<!-- Here, by using the onclick="" we are asking for a confirmation, if cinfirms the the page will send to the link with album_id -->
<!-- onclick id a javascript -->
<a href="{% url 'delete_album' album_id %}" class="btn btn-danger" onclick= " return confirm('Delete this Album?')" >Delete</a>

```
### step2: grab the id value at urls.py
```
path('delete_album/<int:album_id>', views.delete_album, name='delete_album'), # album_id, grabs the id value and pass to views
```
### step3: views.py
```
def delete_album(req, album_id):
    dict={'title': 'Edit Album'}

    album= get_object_or_404(Album, id=album_id)        # geting the particular album , by album id
    
    # Here we also could use
    # album= Album.objects.get(id=album_id) ## same
    dict['success'] = "Album deleted!"

    album.delete()                                      # deleting the record from database
    
    return render(req, 'first_app/delete_album.html', context=dict )
```
