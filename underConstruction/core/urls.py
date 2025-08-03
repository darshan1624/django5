from django.urls import path
from core import views

urlpatterns = [
    path('', views.home_page, name='home_page'),
    path('About/', views.about_page, name='about_page'),
    path('Contact/', views.contact_page, name='contact_page'),
]
