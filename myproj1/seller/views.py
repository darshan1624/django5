from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from account.decorators import outer_decorator_require_roles

@outer_decorator_require_roles('seller')
def seller_dashboard_view(request):
    return render(request, 'seller/dashboard.html')
