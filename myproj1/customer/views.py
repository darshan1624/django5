from django.shortcuts import render, redirect
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib import messages
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from account.decorators import outer_decorator_require_roles


@outer_decorator_require_roles('customer')
def customer_dashboard_view(request):
    return render(request, 'customer/dashboard.html')


@login_required
def password_change_view(request):
    return render(request, 'customer/password_change.html')
