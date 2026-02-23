from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('returns/', views.returns, name='returns'),
    path('shipping/', views.shipping, name='shipping'),
    path('faq/', views.faq, name='faq'),
    path('contact/', views.contact, name='contact'),
    path('privacy-policy/', views.privacy, name='privacy-policy'),
]
