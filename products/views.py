from django.contrib import messages
from django.shortcuts import redirect, reverse, render, get_object_or_404
from django.db.models import Q
from django.db.models.functions import Lower
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_POST
from django.contrib.auth.decorators import user_passes_test
from django.utils import timezone
from .models import Product, Category, ProductReview
from .forms import ProductForm
from .forms import ProductReviewForm


def is_commenter_or_superuser(user, review: ProductReview) -> bool:
    return user.is_superuser or review.user_id == user.id


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
            products = products.annotate(
                lower_category=Lower('category__friendly_name')
            )
            sortkey = 'lower_category'

        if direction == 'desc':
            sortkey = f'-{sortkey}'

        products = products.order_by(sortkey)
    else:
        products = products.order_by('name')

    current_sorting = f'{sort}_{direction}' if sort else None
    available_categories = (
        Category.objects
        .filter(products__in=products)
        .distinct()
        .order_by('friendly_name')
    )

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

    if request.method == "POST" and request.user.is_authenticated:
        form = ProductReviewForm(request.POST)

        # prevent duplicate review
        already_reviewed = ProductReview.objects.filter(
            product=product,
            user=request.user
        ).exists()

        if already_reviewed:
            messages.info(request, "You have already reviewed this product.")
            return redirect("product_detail", product_slug=product.slug)

        if form.is_valid():
            review = form.save(commit=False)
            review.product = product
            review.user = request.user
            review.status = ProductReview.Status.PENDING
            review.save()

            messages.success(
                request,
                (
                    "Your review has been submitted and"
                    "is awaiting approval."
                ),
            )
            return redirect("product_detail", product_slug=product.slug)
    else:
        form = ProductReviewForm()

    context = {
        'product': product,
        'review_form': form,
    }

    return render(request, 'products/product_details.html', context)


@login_required
def add_product(request):
    """ Add a product to the store """
    if not request.user.is_superuser:
        messages.error(request, "Sorry, only store owners can do that.")
        return redirect(reverse('home'))

    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            product = form.save()
            messages.success(
                request, f'Product "{product.name}" added successfully!'
                )
            return redirect(reverse('product_detail', args=[product.slug]))
        else:
            messages.error(
                request,
                (
                    "Failed to add product. Please check "
                    "the form for errors."
                ),
            )
    else:
        form = ProductForm()

    context = {
        'form': form,
    }
    return render(request, 'products/add_product.html', context)


@login_required
def amend_product(request, product_slug):
    """Edit a product in the store"""
    if not request.user.is_superuser:
        messages.error(request, "Sorry, only store owners can do that.")
        return redirect(reverse("home"))

    product = get_object_or_404(Product, slug=product_slug)

    if request.method == "POST":
        post = request.POST.copy()

        if "is_dice_set" not in post:
            if product.is_dice_set:
                post["is_dice_set"] = "on"
            else:
                post["is_dice_set"] = ""

        form = ProductForm(post, request.FILES, instance=product)

        if form.is_valid():
            product = form.save()
            messages.success(
                request, f'Product "{product.name}" updated successfully!'
                )
            return redirect(reverse("product_detail", args=[product.slug]))
        else:
            messages.error(
                request,
                (
                    "Failed to update product. Please check the form "
                    "for errors."
                )
            )
    else:
        form = ProductForm(instance=product)

    return render(
        request, "products/amend_product.html",

        {
            "form": form,
            "product": product

        }
    )


@login_required
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


@login_required
def create_review(request, product_slug):
    product = get_object_or_404(Product, slug=product_slug)

    if (
        ProductReview.objects
        .filter(product=product, user=request.user)
        .exists()
    ):
        messages.info(request, "You’ve already reviewed this product.")
        return redirect("product_detail", product_slug=product.slug)

    if request.method == "POST":
        form = ProductReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.product = product
            review.user = request.user
            review.status = ProductReview.Status.PENDING
            review.save()
            messages.success(
                request, "Thanks! Your review is awaiting approval."
                )
            return redirect("product_detail", product_slug=product.slug)
    else:
        form = ProductReviewForm()

    return render(
        request, "reviews/create_review.html",

        {
            "product": product,
            "form": form

        }
    )


@login_required
@require_POST
def delete_review(request, review_id):
    review = get_object_or_404(ProductReview, id=review_id)

    if not is_commenter_or_superuser(request.user, review):
        messages.error(
            request, "You don’t have permission to delete this review."
            )
        return redirect("product_detail", product_slug=review.product.slug)

    product_slug = review.product.slug
    review.delete()
    messages.success(request, "Review deleted.")
    return redirect("product_detail", product_slug=product_slug)


def staff_required(view_func):
    return user_passes_test(lambda u: u.is_active and u.is_staff)(view_func)


@login_required
@require_POST
def edit_review(request, review_id):
    review = get_object_or_404(ProductReview, id=review_id)

    # only commenter or superuser
    if request.user != review.user:
        messages.error(
            request, "Only the original reviewer can edit this review."
            )
        return redirect("product_detail", product_slug=review.product.slug)

    review.rating = request.POST.get("rating")
    review.title = request.POST.get("title")
    review.body = request.POST.get("body")

    # send back to moderation
    review.status = ProductReview.Status.PENDING
    review.approved_by = None
    review.approved_at = None

    review.save()

    messages.success(request, "Review updated and sent for approval.")
    return redirect("product_detail", product_slug=review.product.slug)


@login_required
@staff_required
@require_POST
def approve_review(request, review_id):
    review = get_object_or_404(ProductReview, id=review_id)
    review.status = ProductReview.Status.APPROVED
    review.approved_at = timezone.now()
    review.approved_by = request.user
    review.save(update_fields=["status", "approved_at", "approved_by"])
    messages.success(request, "Review approved.")
    return redirect("product_detail", product_slug=review.product.slug)


@login_required
@staff_required
@require_POST
def reject_review(request, review_id):
    review = get_object_or_404(ProductReview, id=review_id)
    review.status = ProductReview.Status.REJECTED
    review.approved_at = None
    review.approved_by = None
    review.save(update_fields=["status", "approved_at", "approved_by"])
    messages.info(request, "Review rejected.")
    return redirect("product_detail", product_slug=review.product.slug)
