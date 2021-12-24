from django.conf.urls import url
from django.urls import path
from . import views
urlpatterns = [
  path('', views.homePage, name='homePage'),
  path('album_list/<int:artist_id>', views.album_list, name='album_list'),
  path('musician_form/', views.musician_form, name='musician_form'),
  path('album_form', views.album_form, name='album_form'),
  path('edit_album/<int:album_id>', views.edit_album, name='edit_album'),
  path('delete_album/<int:album_id>', views.delete_album, name='delete_album'),

  path('form', views.form, name='form'),
  path('index/', views.index, name='index'),
]
