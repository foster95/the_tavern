from django.urls import path
from . import views

urlpatterns = [
    path('', views.product_list, name='products'),
    path('add/', views.add_product, name='add_product'),
    path('<slug:product_slug>/', views.product_detail, name='product_detail'),
]