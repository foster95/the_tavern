from django.contrib import messages
from django.shortcuts import redirect, reverse
from django.db.models import Q
from django.shortcuts import render, get_object_or_404
from .models import Product

# Create your views here.

def product_list(request):
    """ A view to show all products, including sorting and search queries """

    products = Product.objects.all()
    query = None

    if request.GET:
        if 'q' in request.GET:
            query = request.GET['q']
            if not query:
                messages.error(request, "You didn't enter any search criteria!")
                return redirect(reverse('products'))
            
            queries = Q(name__icontains=query) | Q(description__icontains=query)
            products = products.filter(queries)

    context = {
        'products': products,
        'search_term': request.GET.get('q', ''),
    }
    
    return render(request, 'products/products.html', context)

def product_detail(request, product_slug):
    """ A view to show individual product details """

    product = Product.objects.get(slug=product_slug)

    context = {
        'product': product,
    }

    return render(request, 'products/product_details.html', context)