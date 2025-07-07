from django.shortcuts import render
from student.forms import Registeration, LoginUser
from django.http import HttpResponseRedirect
# Create your views here.


def register(request):
    form =  Registeration(field_order=['email', 'city'], initial={'first_name':'Amit'})
    return render(request, 'student/register.html', context={'fm': form})


def login(request):
    if request.method == 'POST':
        form = LoginUser(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
            username = form.cleaned_data['username']
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            return HttpResponseRedirect('/student/login')
    else: 
        form = LoginUser()
    return render(request, 'student/login.html', context= {'fm': form})
