from django.shortcuts import render
from .models import Product

# Create your views here.
def product_detail(request, slug):
    product = Product.objects.get(slug=slug)

    return render(request, 'store/product_detail.html', {
        'product': product
    })