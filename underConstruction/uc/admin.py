from django.contrib import admin
from uc.models import UnderConstructModel
# Register your models here.

class UnderConstructModelAdmin(admin.ModelAdmin):
    list_display = ['uc_note', 'uc_duration', 'is_under_construct', 'updated_at']

admin.site.register(UnderConstructModel, UnderConstructModelAdmin)