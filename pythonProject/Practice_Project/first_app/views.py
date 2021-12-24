
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from first_app.models import Musician, Album


from first_app.forms import MusicianForm, AlbumForm



def homePage(req):
    read = Musician.objects.all().order_by('first_name') # grab all the records from database of Musician table, using ORDER by

    diction = {'title': "Home Page", 'musician_list': read} # passing all the records to html page
    return render(req, 'first_app/home.html', context=diction)

def album_list(req, artist_id):                              # by artist_id variable we are receiving the value of id
    # here if we need the we can get the musician info
    # artist= Musician.objects.get( id=artist_id )
    # or
    # details = get_object_or_404(Musician, id= artist_id) # but for htis we need a library to import
    # (from django.shortcuts import get_object_or_404)

    albums_of_MU = Album.objects.filter(artist= artist_id).order_by('-num_stars', 'name')   # using foreign key value mathcing for filter

    diction={'title': "List of Album", "album":albums_of_MU,'artist': albums_of_MU[0].artist }
    return render(req, 'first_app/album_list.html', context=diction)

def musician_form(req):
    form= MusicianForm() # creating object of MusicianForm
    
    if req.method == 'POST':            # if form submited
        form = MusicianForm(req.POST)   # grabing the form

        if form.is_valid():             # checking form is valid or not
            form.save(commit=True)      # saving to the database
            return homePage(req)        # if form saved the we will redirect to home page

    diction={'title': 'Add Musician', 'musician_form': form}
    return render(req, 'first_app/musician_form.html', context=diction)

def album_form(req):
    form = AlbumForm()  # creating object of AlbumForm

    if req.method == 'POST':             # if form submited
        form = AlbumForm(req.POST)       # grabing the form

        if form.is_valid():             # checking form is valid or not
            form.save(commit=True)      # saving to the database
            return homePage(req)        # if form saved the we will redirect to home page

    diction= {'title': 'Add Album', 'album_form':form}
    return render(req, 'first_app/album_form.html', context=diction)
def edit_album(req, album_id):
    dict={'title': 'Edit Album'}

    album= get_object_or_404(Album, id=album_id)        # geting the particular album , by album id
    # Here we also could use
    # album= Album.objects.get(id=album_id) ## same

    form= AlbumForm( instance = album)                  # form obj with previously filled value, 'instance=album' gives the previous value

    if req.method=='POST':
        form = AlbumForm(req.POST, instance= album)     # Grab the new filled info into previously filled form obj
        if form.is_valid: # checking the input is valid or not
            form.save(commit=True) # saving to database, exactly in the previously filled obj
            dict['success']="updated"

    dict["form"]=form
    dict['album_id']= album_id # needed, when we will delete the album.
    return render(req, 'first_app/edit_album.html', context=dict )

def delete_album(req, album_id):
    dict={'title': 'Edit Album'}

    album= get_object_or_404(Album, id=album_id)        # geting the particular album , by album id
    # Here we also could use
    # album= Album.objects.get(id=album_id) ## same
    dict['success'] = "Album deleted!"
    album.delete()                                      # deleting the record from database
    return render(req, 'first_app/delete_album.html', context=dict )






def index(request):
    musician_list = Musician.objects.all().order_by('first_name')
    return render(request, 'first_app/index.html', {'mu_obj': musician_list})


# Create your views here.
def form2(request):

    pyForm= forms.Mucician() # here, Mucician is the form name. (forms is the forms.py file)

    diction={}
    if request.method == "POST": # if any post request
        submitedForm= forms.Mucician(request.POST) # grab the submitted form
        pyForm = submitedForm
        if submitedForm.is_valid():                              # form validation check
            first_name= submitedForm.cleaned_data['first_name']  # grabing each values
            last_name= submitedForm.cleaned_data['last_name']
            email= submitedForm.cleaned_data['email']
            date_of_birth= submitedForm.cleaned_data['date_of_birth']

            diction.update({'first':first_name})    # thats how we can concatenate with previous dictionary
            diction['last'] =last_name              # thats how we can concatenate with previous dictionary
            diction.update({'email': email})
            diction.update({'dob': date_of_birth})
            diction.update({'form_sub_check': 'yes'})

    diction['pyform']= pyForm
    return render(request, 'first_app/form.html', context=diction)

def form(request):

    pyForm= forms.MusicianForm() # here, Mucician is the form name. (forms is the forms.py file)
    diction={}
    if request.method == "POST": # if any post request
        submitedForm= forms.MusicianForm(request.POST) # grab the submitted form
        pyForm = submitedForm
        if submitedForm.is_valid():                              # form validation check
            submitedForm.save(commit=True)
            return index(request)                               # sending request to another view

    diction['pyform']= pyForm
    return render(request, 'first_app/form.html', context=diction)