from django.shortcuts import render

# Create your views here.
def index_render(request):
    return render(request, 'index.html')

def about_render(request):
    return render(request, 'about.html')

def contact_render(request):
    return render(request, 'contact.html')

def location_render(request):
    return render(request, 'location.html')

def products_render(request):
    return render(request, 'products.html')

def cart_render(request):
    return render(request, 'cart.html')

def category_products_render(request):
    return render(request, 'category_products.html')

def all_products_render(request):
    return render(request, 'all_products.html')

