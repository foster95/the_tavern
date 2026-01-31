from django.shortcuts import render, get_object_or_404
from .models import Product

# Create your views here.

def product_list(request):
    """ A view to show all products, including sorting and search queries """

    products = Product.objects.all()

    context = {
        'products': products,
    }
    
    return render(request, 'products/products.html', context)

def product_detail(request, product_slug):
    """ A view to show individual product details """

    product = Product.objects.get(slug=product_slug)

    context = {
        'product': product,
    }

    return render(request, 'products/product_details.html', context)