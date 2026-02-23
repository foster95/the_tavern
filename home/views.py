from django.shortcuts import render, redirect
from django.utils import timezone
from .models import ProductOfTheMonth, Testimonial
from .forms import ContactMessageForm
from django.contrib import messages


def home(request):
    """
    Renders the home page.
    """
    today = timezone.localdate()

    potm = (
        ProductOfTheMonth.objects
        .select_related("product")
        .filter(year=today.year, month=today.month)
        .first()
    )

    testimonials = (
        Testimonial.objects
        .order_by("sort_order", "-created_at")[:3]
    )

    return render(request, "home/index.html", {
        "product_of_the_month": potm.product if potm else None,
        "testimonials": testimonials
    })

def about(request):
    return render(request, "home/about.html")

def returns(request):
    return render(request, "home/returns.html")

def shipping(request):
    return render(request, "home/shipping.html")

def faq (request):
    return render(request, "home/faq.html")

def contact(request):
    if request.method == "POST":
        form = ContactMessageForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Thanks! Your message has been sent.")
            return redirect("contact")
    else:
        form = ContactMessageForm()

    return render(request, "home/contact.html", {"form": form})
