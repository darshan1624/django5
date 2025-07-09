from django.shortcuts import render, redirect

def home(request):
    return render(request, 'account/home.html')


def login_view(request):
    return render(request, 'account/login.html')


def register_view(request):
    return render(request, 'account/register.html')

def password_reset_view(request):
    return render(request, 'account/password_reset.html')
