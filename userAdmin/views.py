from django.shortcuts import render
from django.http import HttpResponse, HttpRequest, HttpResponseRedirect
from django.contrib.auth.models import User, Group
from django.urls import reverse
from django.contrib.auth import authenticate, login, logout


def signup(request: HttpRequest):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']

        group_user = Group.objects.get(name='user')

        user = User.objects.create_user(username, email, password)
        user.groups.add(group_user)
        user.save()

        return HttpResponseRedirect(reverse('login'))
    else:
        return render(request, 'userAdmin/signup.html')


def login_user(request: HttpRequest):
    if request.method == 'POST':
        username = request.POST['userName']
        password = request.POST['password']

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse('get-cars'))

        return render(request, 'userAdmin/login.html')

    else:
        return render(request, 'userAdmin/login.html')


def logout_user(request: HttpRequest):
    logout(request)
    return HttpResponseRedirect(reverse('login_user'))
