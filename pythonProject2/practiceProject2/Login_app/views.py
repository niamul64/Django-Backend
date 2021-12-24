from django.shortcuts import render

# Create your views here.

def index(req):
    dict={'Title': 'Index Page',}

    return render(req, 'Login_app/index.html', context=dict)