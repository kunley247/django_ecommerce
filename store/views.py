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

def dashboardView(request):
    category = Category.objects.filter(status=0)
    context = {'category':category}
    return render(request, "bootstrap/dashboard.html", context)

def categoryView(request, slug):
    if ( Category.objects.filter(slug=slug, status=0) ):
        products = Product.objects.filter(category__slug=slug)
        context = {'products':products, 'category_slug': slug}
        return render(request, "bootstrap/products.html", context)
    else:
        messages.warning(request, "No such category found.")
        return redirect("dashboard")
    

def productsView(request, slug, category_slug=""):
    if ( Product.objects.filter(slug=slug, status=0) ):
        
        category_slug = request.GET.get('category_slug')
        products = Product.objects.filter(category__slug=category_slug)
        services = Services.objects.filter(product__slug=slug)
        
        context = {
            'services': services,
            'products': products,
            'category_slug': category_slug,
            'product_slug': slug
        }

        return render(request, "bootstrap/products.html", context)
    else:
        messages.warning(request, "No such product found.")
        return render(request, "category")
