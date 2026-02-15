from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404
from django.contrib import messages

from .models import UserProfile
from .forms import UserProfileForm
from checkout.models import Order


@login_required
def profile(request):
    profile = get_object_or_404(UserProfile, user=request.user)

    if request.method == "POST":
        # Upload picture
        if "update_picture" in request.POST and request.FILES.get("profile_picture"):
            profile.profile_picture = request.FILES["profile_picture"]
            profile.save()
            messages.success(request, "Profile picture updated.")

        # Remove picture
        elif "remove_picture" in request.POST:
            profile.profile_picture = None
            profile.save()
            messages.success(request, "Profile picture removed.")

        # Update delivery fields
        elif "update_delivery" in request.POST:
            form = UserProfileForm(request.POST, instance=profile)
            if form.is_valid():
                form.save()
                messages.success(request, "Profile updated successfully.")

    form = UserProfileForm(instance=profile)
    orders = profile.orders.all()

    return render(request, "profiles/profile.html", {
        "profile": profile,
        "form": form,
        "orders": orders,
        "on_profile_page": True,
    })


def order_history(request, order_number):
    """ Display the user's order history """
    order = get_object_or_404(Order, order_number=order_number)

    messages.info(request, 
                  f"This is a past confirmation for order number {order_number}. "
                  "A confirmation email was sent on the order date.")
    
    template = "checkout/checkout_success.html"
    context = {
        "order": order,
        "from_profile": True,
    }
    return render(request, template, context)