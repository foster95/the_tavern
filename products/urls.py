from django.urls import path
from . import views

urlpatterns = [
    path('', views.product_list, name='products'),
    path('add/', views.add_product, name='add_product'),
    path("reviews/<int:review_id>/edit/", views.edit_review, name="edit_review"),
    path("reviews/<int:review_id>/delete/", views.delete_review, name="delete_review"),
    path("<int:review_id>/approve/", views.approve_review, name="approve_review"),
    path("<int:review_id>/reject/", views.reject_review, name="reject_review"),
    path('amend/<slug:product_slug>/', views.amend_product, name='amend_product'),
    path('delete/<slug:product_slug>/', views.delete_product, name='delete_product'),
    path('<slug:product_slug>/', views.product_detail, name='product_detail'),
]