from django.shortcuts import render
from .models import Product

def store(request):
    products = Product.objects.all()
    context = {
        'products': products,
    }

    return render(request, 'index.html',context)

def about(request):
    return render(request, 'about2.html')


def contactus(request):
    return render(request, 'contact-us.html')

def productInfo(request,id):
    product = Product.objects.get(pk=id)
    context = {'product':product}
    return render(request, 'product-details.html',context)
