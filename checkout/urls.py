from django.urls import path
from . import views
from .webhooks import webhook

urlpatterns = [
    path("", views.checkout, name="checkout"),
    path("order-confirmation/<order_number>/", views.order_confirmation, name="order_confirmation"),
    path("wh/", webhook, name="webhook"),
]