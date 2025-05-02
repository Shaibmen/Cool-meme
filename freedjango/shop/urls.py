from django.urls import path
from .views import *


urlpatterns = [
    path('', index_render, name='index_render'),
    path('about', about_render, name='about_render'),
    path('about/contact', contact_render, name='contact_render'),
    path('about/location', location_render, name='location_render'),
    path('products', products_render, name='products_render'),
    path('cart', cart_render, name='cart_render'),
    path('products/categoryproducts', category_products_render, name='category_products_render'),
    path('products/allproducts', all_products_render, name='all_products_render'),
    # path('cloth/', ClothListView.as_view(), name='clothes_list'),
    # path('cloth/<int:pk>/', ClothDetailView.as_view(), name='clothes_detail'),
    # path('cloth/create', ClothCreateView.as_view(), name='clothes_create'),
    # path('cloth/<int:pk>/update/', ClothUpdateView.as_view(), name='clothes_update'),
    # path('cloth/<int:pk>/delete/', ClothDeleteView.as_view(), name='clothes_delete'),
    # велосипеды
    path('bicycle/', BicycleListView.as_view(), name='bicycle_list'),
    path('bicycle/<int:pk>/', BicycleDetailView.as_view(), name='bicycle_detail'),
    path('bicycle/create', BicycleCreateView.as_view(), name='bicycle_create'),
    path('bicycle/<int:pk>/update/', BicycleUpdateView.as_view(), name='bicycle_update'),
    path('bicycle/<int:pk>/delete/', BicycleDeleteView.as_view(), name='bicycle_delete'),

    # bicycle_photo
    path('bicycle_photo/', PhotoBicycleListView.as_view(), name='bicycle_photo_list'),
    path('bicycle_photo/<int:pk>/', PhotoBicycleDetailView.as_view(), name='bicycle_photo_detail'),
    path('bicycle_photo/create', PhotoBicycleCreateView.as_view(), name='bicycle_photo_create'),
    path('bicycle_photo/<int:pk>/update/', PhotoBicycleUpdateView.as_view(), name='bicycle_photo_update'),
    path('bicycle_photo/<int:pk>/delete/', PhotoBicycleDeleteView.as_view(), name='bicycle_photo_delete'),

    # galery 
    path('galery/', GaleryListView.as_view(), name='galery_list'),
    path('galery/<int:pk>/', GaleryDetailView.as_view(), name='galery_detail'),
    path('galery/create', GaleryCreateView.as_view(), name='galery_create'),
    path('galery/<int:pk>/update/', GaleryUpdateView.as_view(), name='galery_update'),
    path('galery/<int:pk>/delete/', GaleryDeleteView.as_view(), name='galery_delete'),
]
