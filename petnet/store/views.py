from django.shortcuts import render
from .models import Product

# Create your views here.
def product_detail(request, slug):
    print('Slug:', slug)
    return render(request, 'store/product_detail.html')