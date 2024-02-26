from django.shortcuts import render
from django.http import HttpResponse, HttpRequest
from django.contrib.auth.models import User, Group


def signup(request: HttpRequest):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']

        group_user = Group.objects.get(name='user')

        user = User.objects.create_user(username, email, password)
        user.groups.add(group_user)
        user.save()

        return HttpResponse('Signup')
    else:
        return render(request, 'userAdmin/signup.html')


def login(request: HttpRequest):
    if request.method == 'POST':
        return HttpResponse('Login')
    else:
        return render(request, 'userAdmin/login.html')
