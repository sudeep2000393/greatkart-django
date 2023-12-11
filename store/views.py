from django.shortcuts import render, get_object_or_404
from .models import Product, Category


def store(request, category_slug=None):
    categories = None
    products = None

    if category_slug:
        categories = get_object_or_404(Category, slug=category_slug)
        products = Product.objects.filter(
            category=categories, is_available=True)
        product_count = products.count()
    else:
        products = Product.objects.filter(is_available=True)
        product_count = products.count()

    context = {
        'products': products,
        'product_count': product_count
    }
    return render(request, 'store/store.html', context)


def product_detail(request, category_slug, product_slug):
    single_product = get_object_or_404(
        Product, category__slug=category_slug, slug=product_slug)
    is_out_of_stock = single_product.stock <= 0

    context = {
        'single_product': single_product,
        'is_out_of_stock': is_out_of_stock,
    }

    return render(request, 'store/product_detail.html', context)
