from django.http import HttpResponseRedirect
from django.shortcuts import render,redirect
from .models import Users
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login as authlogin,logout
# Create your views here.
def login(request):
    if ('loginid' not in request.session):
        if (request.method == 'GET'):
            return render(request, 'login.html', {})
        else:
            user = Users.objects.filter(name=request.POST['your_name'], password=request.POST['password'])
            authuser = authenticate(username=request.POST['your_name'],
                                    password=request.POST['password'])
            if (len(user) != 0 and authuser is not None):
                authlogin(request, authuser)
                request.session['loginid'] = user[0].id
                request.session['loginname'] = user[0].name

                return redirect('/trainee/list')

            else:
                return render(request, 'login.html', {'error': 'invalid credentails'})
    else:
        return redirect('/trainee/list')

def register(request):
    if (request.method == 'GET'):
        return render(request, 'register.html')
    else:
        if request.POST['password'] == request.POST['re_pass']:
            Users.objects.create(name=request.POST['name'], email=request.POST['email'],
                                    password=request.POST['password'])
            User.objects.create_superuser(username=request.POST['name'], email=request.POST['email'],
                                     password=request.POST['password'],is_staff=True)
            return HttpResponseRedirect("/trainee/list/")


        else:
            return render(request, 'register.html', {'error': 'invalid'})

def Logout(request):
    logout(request)
    return HttpResponseRedirect("/myuser/login/")
