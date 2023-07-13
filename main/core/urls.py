from django.urls import path
from . import views

app_name ='main.core'

urlpatterns =[
    path('', views.home, name='home' ),
    
]

