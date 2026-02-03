from decimal import Decimal
from django.conf import settings

def bag_contents (request):
    """
    Context processor to retrieve the shopping bag contents
    and make it available across all templates
    """
    bag = request.session.get('bag', {})

    bag_items = []
    total = 0
    product_count = 0

    if total < settings.FREE_DELIVERY_THRESHOLD:
        delivery = total * Decimal(settings.STANDARD_DELIVERY_PERCENTAGE)
        free_delivery_delta = settings.FREE_DELIVERY_THRESHOLD - total
    else:
        delivery = 0
        free_delivery_delta = 0

    grand_total = delivery + total

    for item_id, item_data in bag.items():
        product_count += item_data['quantity']
        price = item_data['price']
        total += item_data['quantity'] * price
        bag_items.append({
            'item_id': item_id,
            'quantity': item_data['quantity'],
            'price': price,
            'total_price': item_data['quantity'] * price,
        })

    grand_total = total 

    context = {
        'bag_items': bag_items,
        'total': total,
        'product_count': product_count,
        'delivery': delivery,
        'free_delivery_delta': free_delivery_delta,
        'free_delivery_threshold': settings.FREE_DELIVERY_THRESHOLD,
        'grand_total': grand_total,
    }

    return context