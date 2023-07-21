from django.urls import path
from . import views

app_name = 'gallery'

urlpatterns = [
	path('new-gallery/', views.createAlbum, name='new_gallery'),
	path('new-photo/<int:pk>/', views.photo, name='new_photo'),
	path('select-photo/<int:pk>/', views.selectPhoto, name='change_photo'),
]