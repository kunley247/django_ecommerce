from django.contrib import messages
from django.shortcuts import redirect, render 
from .models import *

# Create your views here.

def home(request):
    return render(request, "bootstrap/index.html")

def register(request):
    return render(request, "bootstrap/register.html")

def login(request):
    return render(request, "bootstrap/login.html")

def password(request):
    return render(request, "bootstrap/password.html")


def collections(request):
    category = Category.objects.filter(status=0)
    context = {'category':category}
    return render(request, "bootstrap/collections.html", context)

def collectionsView(request, slug):
    if ( Category.objects.filter(slug=slug, status=0) ):
        products = Product.objects.filter(category__slug=slug)
        context = {'products':products}
        return render(request, "bootstrap/products.html", context)
    else:
        messages.warning(request, "No such category found.")
        return redirect("collections")
    

def productsView(request, slug):
    if ( Product.objects.filter(slug=slug, status=0) ):
        services = Services.objects.filter(product__slug=slug)
        context = {'services':services}
        return render(request, "bootstrap/services.html", context)
    else:
        messages.warning(request, "No such product found.")
        return render(request, "bootstrap/services.html")
