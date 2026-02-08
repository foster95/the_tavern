from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from products.models import Product


# Create your views here.

def view_bag(request):
    """ A view to return the shopping bag page """
    return render(request, 'bag/bag.html')

def add_to_bag(request, item_id):
    product = get_object_or_404(Product, pk=item_id)
    quantity = int(request.POST.get("quantity", 1))
    redirect_url = request.POST.get("redirect_url", "/")

    dice_option = request.POST.get("dice_option")  # "single" or "set" or None

    bag = request.session.get("bag", {})

    bag_key = f"{item_id}:set" if dice_option == "set" else str(item_id)

    bag[bag_key] = bag.get(bag_key, 0) + quantity
    request.session["bag"] = bag
    messages.success(request, f'Added {product.name} to your Bag of Holding.')

    return redirect(redirect_url)

def adjust_bag(request, item_id):
    try: 
        quantity = int(request.POST.get("quantity", 1))
        dice_option = request.POST.get("dice_option")  # "single" or "set" or None

        bag = request.session.get("bag", {})
        bag_key = f"{item_id}:set" if dice_option == "set" else str(item_id)

        if quantity > 0:
            bag[bag_key] = quantity
        else:
            bag.pop(bag_key, None)

        request.session["bag"] = bag
        return redirect("view_bag")
    except Exception as e:
        print(f"Error adjusting bag: {e}")
        return redirect("view_bag")

def remove_from_bag(request, item_id):
    try: 
        dice_option = request.POST.get("dice_option")  # "single" or "set" or None

        bag = request.session.get("bag", {})
        bag_key = f"{item_id}:set" if dice_option == "set" else str(item_id)

        bag.pop(bag_key, None)

        request.session["bag"] = bag
        return redirect("view_bag")
    except Exception as e:
        print(f"Error removing item from bag: {e}")
        return redirect("view_bag")