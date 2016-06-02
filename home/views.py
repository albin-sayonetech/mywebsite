from django.shortcuts import render,HttpResponse
from .models import Event
from login.models import UserDetails

# Create your views here.



def events(request):
    return render(request, 'test.html', {})