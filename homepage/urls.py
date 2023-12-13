from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('About', views.About, name='About'),
    path('Services', views.Services, name='Services'),
    path('Contact', views.Contact, name='Contact'),
    path('Redirect', views.Redirect, name='Redirect'),
]