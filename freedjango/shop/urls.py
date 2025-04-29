from django.urls import path
from .views import *


urlpatterns = [
    path('index', index_render, name='index_render'),
    path('about', about_render, name='about_render'),
    path('about/contact', contact_render, name='contact_render'),
    path('about/location', location_render, name='location_render'),
    path('products', products_render, name='products_render'),
    path('cart', cart_render, name='cart_render'),
    path('products/categoryproducts', category_products_render, name='category_products_render'),
    path('products/allproducts', all_products_render, name='all_products_render'),
    
]
