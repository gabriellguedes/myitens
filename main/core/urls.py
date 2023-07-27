from django.urls import path
from main.accounts.views import user_profile
from . import views

app_name ='core'

urlpatterns =[
    path('', views.home, name='home' ),
    path('<str:pk>/', user_profile, name='user_profile'),
    
]

