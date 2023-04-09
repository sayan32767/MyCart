from django.shortcuts import render
from django.http import HttpResponse
from .models import Product

# Create your views here.
def index(request):
    products = Product.objects.values_list('product_name')

    products = [product[0].replace("'(),", "").title() for product in products]

    params = {
        'products': products
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
