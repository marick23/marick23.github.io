from django.shortcuts import render
from .models import Product

def index(request):
    products = Product.objects.all().order_by('-pk')

    return render(
        request,
        'product/product_list.html',
        {
            'products': products
        }
    )