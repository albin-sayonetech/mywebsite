from django.shortcuts import render,HttpResponse,HttpResponseRedirect
from login.models import UserDetails


def register(request):
   if request.method=='POST':
           user = UserDetails()
           usernamepass = request.POST.get('username', False)
           passwordpass = request.POST.get('password', False)
           emailpass = request.POST.get('email', False)
           user.username=request.POST['username']
           user.password =request.POST['password']
           user.email =request.POST['email']
           if not user.password or not user.username or not user.email:
               return render(request, 'register.html', {"error":"please fill in all details"})

           elif UserDetails.objects.filter(username= usernamepass).exists():
               return render(request, 'register.html', {"error": "username already exists"})
           elif UserDetails.objects.filter(email=emailpass).exists():
               return render(request, 'register.html', {"error": "email already registered"})
           else:
               user.save()
               return render(request, 'login.html', {"sucess": "successfully created account"})

   else:
       return render(request, 'register.html', {})
