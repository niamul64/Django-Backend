from django.shortcuts import render
from django.http import HttpResponse
from first_app.models import Musician, Album
from first_app import forms

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