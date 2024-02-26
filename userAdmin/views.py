from django.shortcuts import render
from django.http import HttpResponse, HttpRequest


def signup(request: HttpRequest):
    if request.method == 'POST':
        return HttpResponse('Signup')
    else:
        return render(request, 'userAdmin/signup.html')


def login(request: HttpRequest):
    if request.method == 'POST':
        return HttpResponse('Login')
    else:
        return render(request, 'userAdmin/login.html')
