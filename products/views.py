from django.contrib import messages
from django.shortcuts import redirect, reverse, render, get_object_or_404
from django.db.models import Q
from django.db.models.functions import Lower
from .models import Product, Category

# Create your views here.

def product_list(request):
    """ Show all products """

    products = Product.objects.all().order_by('name')  # ✅ always safe
    query = None
    categories = None

    if request.GET:
        # Filter by category
        if 'category' in request.GET:
            category_slugs = request.GET.get('category', '').split(',')
            products = products.filter(category__slug__in=category_slugs)
            categories = Category.objects.filter(slug__in=category_slugs)

        # Search
        if 'q' in request.GET:
            query = request.GET.get('q', '')
            if not query:
                messages.error(request, "You didn't enter any search criteria!")
                return redirect(reverse('products'))

            products = products.filter(
                Q(name__icontains=query) |
                Q(description__icontains=query)
            )

        sort = request.GET.get('sort', '')
        direction = request.GET.get('direction')

        if sort:
            sortkey= sort

            if sortkey == 'name':
                products = products.annotate(lower_name=Lower('name'))
                sortkey = 'lower_name'

            elif sortkey == 'category':
                products = products.annotate(lower_category=Lower('category__friendly_name'))
                sortkey = 'lower_category'
            
            if direction == 'desc':
                sortkey = f'-{sortkey}'
            
            products = products.order_by(sortkey)
        
        else:
            products = products.order_by('name')

        current_sorting = f'{sort}_{direction}'

            

    context = {
        'products': products,
        'search_term': query or '',
        'current_categories': categories,
    }

    return render(request, 'products/products.html', context)

def product_detail(request, product_slug):
    """ A view to show individual product details """

    product = get_object_or_404(Product, slug=product_slug)

    context = {
        'product': product,
    }

    return render(request, 'products/product_details.html', context)