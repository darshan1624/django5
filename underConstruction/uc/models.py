from django.db import models

# Create your models here.

class UnderConstructModel(models.Model):
    uc_note = models.TextField(null=True, blank=True, max_length=800)
    uc_duration = models.DateTimeField(blank=True, null=True)
    is_under_construct = models.BooleanField(default=False)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'Under Construction: {self.is_under_construct}'