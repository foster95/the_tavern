from django.shortcuts import render, redirect, get_object_or_404

# Create your views here.

def view_bag(request):
    """ A view to return the shopping bag page """
    return render(request, 'bag/bag.html')

def add_to_bag(request, item_id):
    quantity = int(request.POST.get("quantity", 1))
    redirect_url = request.POST.get("redirect_url", "/")

    dice_option = request.POST.get("dice_option")  # "single" or "set" or None

    bag = request.session.get("bag", {})

    bag_key = f"{item_id}:set" if dice_option == "set" else str(item_id)

    bag[bag_key] = bag.get(bag_key, 0) + quantity
    request.session["bag"] = bag

    return redirect(redirect_url)