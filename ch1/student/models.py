from django.db import models

# Create your models here.

class Profile(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField(max_length=200)
    city = models.CharField(max_length=200)
    roll = models.IntegerField()
    state = models.CharField(max_length=200)
    comment = models.CharField(max_length=200, default='No comments')