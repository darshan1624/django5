from django.shortcuts import render
from student.forms import Registeration
# Create your views here.


def register(request):
    form =  Registeration(field_order=['email', 'city'], initial={'first_name':'Amit'})
    return render(request, 'student/register.html', context={'fm': form})
