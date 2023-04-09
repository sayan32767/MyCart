from django.shortcuts import render
from django.http import HttpResponse
from .models import Product
from math import ceil

# Create your views here.
def index(request):
    products = Product.objects.all()
    n = len(products)
    nSlides = n // 4 + ceil((n / 4) - (n // 4))
    params = {
        'products': products,
        'nslides': nSlides,
        'range': range(1, nSlides),
    }
    return render(request, 'shop/index.html', params)


def about(request):
    return render(request, 'shop/about.html')


def contact(request):
    return render(request, 'shop/index.html')


def tracker(request):
    return render(request, 'shop/index.html')


def search(request):
    return render(request, 'shop/index.html')


def productView(request):
    return render(request, 'shop/index.html')


def checkout(request):
    return render(request, 'shop/index.html')
