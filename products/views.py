from django.contrib import messages
from django.shortcuts import redirect, reverse, render, get_object_or_404
from django.db.models import Q
from django.db.models.functions import Lower
from .models import Product, Category

# Create your views here.

def product_list(request):
    """ A view to show all products, including sorting and search queries """

    products = Product.objects.all()
    query = None

    categories = None          
    sort = None
    direction = None

    if request.GET:
        if 'sort' in request.GET:
            sort = request.GET.get('sort')          
            direction = request.GET.get('direction', 'asc') 
            sortkey = sort

        if sortkey == 'name':
            products = products.annotate(lower_name=Lower('name'))
            sortkey = 'lower_name'

        elif sortkey == 'category':
            products = products.annotate(lower_category=Lower('category__friendly_name'))
            sortkey = 'lower_category'

        if direction == 'desc':
            sortkey = f'-{sortkey}'

        products = products.order_by(sortkey)

        if 'category' in request.GET:
            category_slugs = request.GET.get('category', '').split(',')
            products = products.filter(category__slug__in=category_slugs)
            categories = Category.objects.filter(slug__in=category_slugs)

        if 'q' in request.GET:
            query = request.GET.get('q', '')
            if not query:
                messages.error(request, "You didn't enter any search criteria!")
                return redirect(reverse('products'))

            products = products.filter(
                Q(name__icontains=query) | Q(description__icontains=query)
            )

    current_sorting = f"{sort}_{direction}" if sort and direction else None

    context = {
        'products': products,
        'search_term': query or '',
        'current_categories': categories,
        'current_sorting': current_sorting,
    }

    return render(request, 'products/products.html', context)

def product_detail(request, product_slug):
    """ A view to show individual product details """

    product = Product.objects.get(slug=product_slug)

    context = {
        'product': product,
    }

    return render(request, 'products/product_details.html', context)