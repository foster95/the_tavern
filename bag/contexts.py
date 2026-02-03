from decimal import Decimal
from django.conf import settings
from products.models import Product
from django.shortcuts import get_object_or_404

def bag_contents(request):
    """
    Context processor to retrieve the shopping bag contents
    and make it available across all templates.
    """
    bag = request.session.get("bag", {})

    bag_items = []
    total = Decimal("0.00")
    product_count = 0

    for item_id, quantity in bag.items():
        quantity = int(quantity)

        product = get_object_or_404(Product, pk=item_id)
        price = product.price

        line_total = price * quantity

        total += line_total
        product_count += quantity

        bag_items.append({
            "item_id": item_id,
            "product": product,
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