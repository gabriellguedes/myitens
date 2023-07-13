from django.shortcuts import render
from django.contrib.auth import authenticate, login
from django.urls import reverse
from django.http import HttpResponseRedirect

# Create your views here.
def home(request):
    template_name='index.html'
    if request.user.is_authenticated: 
        return render(request, template_name)
    else:
        return HttpResponseRedirect(reverse('accounts:login'))
