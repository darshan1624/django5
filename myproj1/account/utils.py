from account.permission_config import PERMISSION_CONFIG
from django.contrib.contenttypes.models import ContentType
from django.contrib.auth.models import Permission

def assign_permissions(user, role):
    role_permission = PERMISSION_CONFIG.get(role, {})
    for model, permission in role_permission.items():
        content_type = ContentType.objects.get(model=model._meta.model_name, app_label = model._meta.app_label)
        for perm in permission:
            perm_object = Permission.objects.get(content_type=content_type, codename=f"{perm}_{model._meta.model_name}")
            # print(perm_object)
            user.user_permissions.add(perm_object)