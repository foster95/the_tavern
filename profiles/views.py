from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages

from .models import UserProfile
from .forms import UserProfileForm
from checkout.models import Order


@login_required
def profile(request):
    profile = get_object_or_404(UserProfile, user=request.user)

    # Default form (always defined)
    form = UserProfileForm(instance=profile)

    if request.method == "POST":

        # Upload / change picture
        if "update_picture" in request.POST:
            uploaded = request.FILES.get("profile_picture")
            if uploaded:
                profile.profile_picture = uploaded
                profile.save()
                messages.success(request, "Profile picture updated.")
            else:
                messages.error(request, "Please choose an image to upload.")

            return redirect("profile")

        # Remove picture
        if "remove_picture" in request.POST:
            profile.profile_picture = None
            profile.save()
            messages.success(request, "Profile picture removed.")
            return redirect("profile")

        # Update delivery info (this one needs to re-render errors if invalid)
        if "update_delivery" in request.POST:
            form = UserProfileForm(request.POST, instance=profile)
            if form.is_valid():
                form.save()
                messages.success(request, "Profile updated successfully.")
                return redirect("profile")
            else:
                messages.error(request, "Failed to update profile. Please check the form for errors.")
                # fall through to render with bound form + errors

    orders = profile.orders.order_by('-date')

    return render(request, "profiles/profile.html", {
        "profile": profile,
        "form": form,
        "orders": orders,
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