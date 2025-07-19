from django.contrib import admin

# Register your models here.

from account.models import User

class UserAdmin(admin.ModelAdmin):
    list_display = ['email', 'name', 'city', 'is_staff', 'is_active', 'is_superuser', 'is_seller', 'is_customer']


admin.site.register(User, UserAdmin)