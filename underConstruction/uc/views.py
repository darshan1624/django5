from django.shortcuts import render

# Create your views here.

def construct_page(request):
    return render(request, 'uc/under_construct.html')