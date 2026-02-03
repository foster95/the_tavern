from decimal import Decimal
from django.conf import settings
from django.shortcuts import get_object_or_404
from products.models import Product


def bag_contents(request):
    """
    Context processor to retrieve the shopping bag contents
    and make it available across all templates.
    Bag keys:
      - "item_id" for normal items / single
      - "item_id:set" for set option
    """
    bag = request.session.get("bag", {})

    bag_items = []
    total = Decimal("0.00")
    product_count = 0

    for bag_key, quantity in bag.items():
        quantity = int(quantity)

        # bag_key is either "item_id" OR "item_id:set"
        option = None
        if ":" in str(bag_key):
            item_id, option = str(bag_key).split(":", 1)
        else:
            item_id = str(bag_key)

        product = get_object_or_404(Product, pk=item_id)

        has_set_option = bool(product.dice_set_price)

        # choose correct price
        if has_set_option and option == "set":
            price = product.dice_set_price
        else:
            price = product.price

        line_total = price * quantity

        total += line_total
        product_count += quantity

        bag_items.append({
            "key": str(bag_key),            
            "item_id": item_id,
            "product": product,
            "option": option,               
            "has_set_option": has_set_option,
            "quantity": quantity,
            "price": price,
            "total_price": line_total,
        })

    free_threshold = Decimal(str(settings.FREE_DELIVERY_THRESHOLD))

    if total > 0 and total < free_threshold:
        delivery_percent = Decimal(str(settings.STANDARD_DELIVERY_PERCENTAGE))
        if delivery_percent > 1:
            delivery_percent = delivery_percent / Decimal("100")

        delivery = (total * delivery_percent).quantize(Decimal("0.01"))
        free_delivery_delta = (free_threshold - total).quantize(Decimal("0.01"))
    else:
        delivery = Decimal("0.00")
        free_delivery_delta = Decimal("0.00")

    grand_total = total + delivery

    return {
        "bag_items": bag_items,
        "total": total,
        "product_count": product_count,
        "delivery": delivery,
        "free_delivery_delta": free_delivery_delta,
        "free_delivery_threshold": free_threshold,
        "grand_total": grand_total,
    }
