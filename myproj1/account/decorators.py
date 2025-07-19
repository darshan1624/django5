from functools import wraps
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse

def outer_decorator_require_roles(role):
    def decorator(func):
        @wraps(func)
        @login_required
        def wrapper(request, *args, **kwargs):
            if role == 'seller' and not request.user.is_seller:
                return HttpResponse('User Must be a seller')
            elif role == 'customer' and not request.user.is_customer:
                return HttpResponse('User Muste be a customer')
            return func(request, *args, **kwargs)
        return wrapper
    return decorator