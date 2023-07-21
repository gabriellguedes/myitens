from django.shortcuts import render
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.urls import reverse
from django.http import HttpResponseRedirect
from main.accounts.models import UserProfile


# Create your views here.
def home(request):
    template_name='index.html'

    if request.user.is_authenticated:
       return render(request, template_name)
    else:
        return HttpResponseRedirect(reverse('accounts:login'))

def newsletter_add(nome, email):
    arquivo = open('email_list.txt', 'a')
    lista = []
    lista.append("('")
    lista.append(nome)
    lista.append("', '")
    lista.append(email)
    lista.append("'), \n")
    arquivo.writelines(lista)
