from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from .forms import OrderForm

# Create your views here.

def checkout(request):
    """ A view to return the checkout page """
    bag = request.session.get("bag", {})
    if not bag:
        messages.error(request, "Your bag is empty. Please add items before checking out.")
        return redirect(reverse("products"))
    
    order_form = OrderForm()
    template = "checkout/checkout.html"
    context = {
        "order_form": order_form,
    }
    return render(request, template, context)