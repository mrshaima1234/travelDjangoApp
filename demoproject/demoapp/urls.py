from django.urls import path
from . import views

urlpatterns = [
    path('home/', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('details/', views.detail, name='detail'),
    path('thanks/', views.thanks, name='thanks'),
    path('', views.demo, name='demo')
]
