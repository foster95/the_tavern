from django.contrib import messages
from django.shortcuts import redirect, reverse, render, get_object_or_404
from django.db.models import Q
from django.db.models.functions import Lower

from .models import Product, Category
from .forms import ProductForm


def product_list(request):
    """ Show all products """

    products = Product.objects.all()
    all_categories = Category.objects.all().order_by('friendly_name')

    query = None
    categories = None

    # Filter by category
    if 'category' in request.GET:
        category_slugs = request.GET.get('category', '').split(',')
        products = products.filter(category__slug__in=category_slugs)
        categories = Category.objects.filter(slug__in=category_slugs)

    # Search functionality
    if 'q' in request.GET:
        query = request.GET.get('q', '').strip()
        if not query:
            messages.error(request, "You didn't enter any search criteria!")
            return redirect(reverse('products'))

        products = products.filter(
            Q(name__icontains=query) |
            Q(description__icontains=query)
        )

    # Sorting
    sort = request.GET.get('sort', '')
    direction = request.GET.get('direction') 

    if sort:
        sortkey = sort

        if sortkey == 'name':
            products = products.annotate(lower_name=Lower('name'))
            sortkey = 'lower_name'
        elif sortkey == 'category':
            sortkey = 'category__friendly_name'
            products = products.annotate(lower_category=Lower('category__friendly_name'))
            sortkey = 'lower_category'

        if direction == 'desc':
            sortkey = f'-{sortkey}'

        products = products.order_by(sortkey)
    else:
        products = products.order_by('name')

    current_sorting = f'{sort}_{direction}' if sort else None
    available_categories = Category.objects.filter(products__in=products).distinct().order_by('friendly_name')
    

    context = {
        'products': products,
        'search_term': query or '',
        'current_categories': categories,
        'available_categories': available_categories,
        'current_sorting': current_sorting,
    }

    return render(request, 'products/products.html', context)


def product_detail(request, product_slug):
    """ A view to show individual product details """

    product = get_object_or_404(Product, slug=product_slug)

    context = {
        'product': product,
    }

    return render(request, 'products/product_details.html', context)

def add_product(request):
    """ Add a product to the store """
    if not request.user.is_superuser:
        messages.error(request, "Sorry, only store owners can do that.")
        return redirect(reverse('home'))

    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            product = form.save()
            messages.success(request, f'Product "{product.name}" added successfully!')
            return redirect(reverse('product_detail', args=[product.slug]))
        else:
            messages.error(request, "Failed to add product. Please check the form for errors.")
    else:
        form = ProductForm()

    context = {
        'form': form,
    }
    return render(request, 'products/add_product.html', context)

def amend_product(request, product_slug):
    """ Edit a product in the store """
    if not request.user.is_superuser:
        messages.error(request, "Sorry, only store owners can do that.")
        return redirect(reverse('home'))

    product = get_object_or_404(Product, slug=product_slug)

    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            product = form.save()
            messages.success(request, f'Product "{product.name}" updated successfully!')
            return redirect(reverse('product_detail', args=[product.slug]))
        else:
            messages.error(request, "Failed to update product. Please check the form for errors.")
    else:
        form = ProductForm(instance=product)

    context = {
        'form': form,
        'product': product,
    }
    return render(request, 'products/amend_product.html', context)

def delete_product(request, product_slug):
    """ Delete a product from the store """
    if not request.user.is_superuser:
        messages.error(request, "Sorry, only store owners can do that.")
        return redirect(reverse('home'))

    product = get_object_or_404(Product, slug=product_slug)

    if request.method == "POST":
        product_name = product.name
        product.delete()
        messages.success(request, f'"{product_name}" deleted successfully!')
        return redirect(reverse('products'))

    return redirect(reverse('product_detail', args=[product.slug]))