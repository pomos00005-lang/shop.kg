from django.shortcuts import render, get_object_or_404
from myshop.models import Category
from product.models import Products


def category_list(request):
    categories = Category.objects.all()
    products = Products.objects.all()

    return render(
        request,
        'product/product_list.html',
        {
            'categories': categories,
            'products': products,   # ← ВАЖНО
        }
    )


def category_products(request, category_id):
    category = get_object_or_404(Category, id=category_id)
    products = category.products.all()  # related_name='products'

    return render(
        request,
        'category_products.html',
        {
            'category': category,
            'products': products,
        }
    )
