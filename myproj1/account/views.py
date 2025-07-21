from django.shortcuts import render, redirect
from account.forms import RegisterationForm
from account.models import User
from django.contrib.auth import authenticate, login, logout
from account.utils import assign_permissions 

def home(request):
    return render(request, 'account/home.html')


def login_view(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        if not email or not password:
            print('Requires both email and password')
            return redirect('login')

        try:
            user = User.objects.get(email=email)
        except:
            print('User doesnot exist with this email')
            return redirect('login')
        
        if not user.is_active:
            print('User is not active')
            return redirect('login')
        
        user = authenticate(request, email=email, password=password)
        if user:
            login(request, user)
            if user.is_seller:
                return redirect('seller_dashboard')
            elif user.is_customer:
                return redirect('customer_dashboard')
            else:
                return redirect('home')
        else:
            print('Check Passoword')
            return redirect('login')
    
    elif request.user.is_authenticated:
        if user.is_seller:
            return redirect('seller_dashboard')
        elif user.is_customer:
            return redirect('customer_dashboard')
        else:
            return redirect('home')
    return render(request, 'account/login.html')

def logout_view(request):
    logout(request)
    return redirect('login')


def register_view(request):
    if request.method == 'POST':
        form =  RegisterationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])
            user.is_active = False
            role = request.POST.get('role')
            print('roleeeeeeeeeeeee', role)
            if role == 'seller':
                user.is_seller = True
            elif role == 'customer':
                user.is_customer = True
            user.save()
            assign_permissions(user, role)
            return redirect('login')
    else:
        form = RegisterationForm()
    return render(request, 'account/register.html', {'form':form})
	

def password_reset_view(request):
    return render(request, 'account/password_reset.html')
