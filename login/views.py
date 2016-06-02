from django.shortcuts import render
from .models import UserDetails
from home.models import Event
# Create your views here.

def login(request):
    if request.method == 'POST':
        user = UserDetails()
        event_list=Event.objects.filter()
        usernamepass= request.POST.get('username', False)
        passwordpass = request.POST.get('password', False)
        if UserDetails.objects.filter(username= usernamepass, password=passwordpass).exists():
            return render(request, 'home.html', {"eve":event_list})
        else:
            return render(request, 'login.html', {"error":"invalid username or password" })

    else:
         return render(request, 'login.html', {})
