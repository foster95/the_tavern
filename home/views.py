from django.shortcuts import render
from django.utils import timezone
from .models import ProductOfTheMonth, Testimonial

def home_view(request):
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
