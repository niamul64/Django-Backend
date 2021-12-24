from django.contrib import admin
from django.urls import path
from django.conf.urls import include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('first_app.urls')), # it will be forwarded to first_app's urls.py file
]
