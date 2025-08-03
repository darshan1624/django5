from django.urls import path
from uc import views

urlpatterns = [
    path('', views.construct_page, name='construct_page')
]
