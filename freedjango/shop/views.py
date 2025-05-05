from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.views.generic import ListView, DeleteView, CreateView, DetailView, UpdateView

from basket.basket import Basket
from basket.forms import BasketAddProductForm, LoginForm, RegistrationForm
from .models import *
from .forms import *

from django.contrib.auth import login, logout

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

#bicycle
class BicycleListView(ListView):
    model = Bicycle
    template_name = 'bicycle_shop/bicycle_list.html'
    context_object_name = 'bicycle'

class BicycleDetailView(DetailView):
    model = Bicycle
    template_name = 'bicycle_shop/bicycle_detail.html'
    context_object_name = 'bicycle'

    def get_context_data(self, **kwargs):
        context =  super().get_context_data(**kwargs)
        context['form_backet'] = BasketAddProductForm()
        return context

class BicycleCreateView(CreateView):
    model = Bicycle
    form_class = BicycleForm
    template_name = 'bicycle_shop/bicycle_form.html'
    success_url = reverse_lazy('bicycle_list')

class BicycleUpdateView(UpdateView):
    model = Bicycle
    form_class = BicycleForm
    template_name = 'bicycle_shop/bicycle_form.html'
    success_url = reverse_lazy('bicycle_list')
    
class BicycleDeleteView(DeleteView):
    model = Bicycle
    template_name = 'bicycle_shop/bicycle_delete.html'
    context_object_name = 'bicycle'
    success_url = reverse_lazy('bicycle_list')

#PhotoBicycle


class PhotoBicycleListView(ListView):
    model = PhotoBicycle
    template_name = 'bicycle_photo/bicycle_photo_list.html'
    context_object_name = 'photo_bicycle'

class PhotoBicycleDetailView(DetailView):
    model = PhotoBicycle
    template_name = 'bicycle_photo/bicycle_photo_detail.html'
    context_object_name = 'photo_bicycle'

class PhotoBicycleCreateView(CreateView):
    model = PhotoBicycle
    form_class = PhotoBicycleForm
    template_name = 'bicycle_photo/bicycle_photo_form.html'
    success_url = reverse_lazy('bicycle_photo_list')

class PhotoBicycleUpdateView(UpdateView):
    model = PhotoBicycle
    form_class = PhotoBicycleForm
    template_name = 'bicycle_photo/bicycle_photo_form.html'
    success_url = reverse_lazy('bicycle_photo_list')
    
class PhotoBicycleDeleteView(DeleteView):
    model = PhotoBicycle
    template_name = 'bicycle_photo/bicycle_photo_delete.html'
    context_object_name = 'photo_bicycle'
    success_url = reverse_lazy('bicycle_photo_list')


#galery

class GaleryListView(ListView):
    model = Galery
    template_name = 'galery/galery_list.html'
    context_object_name = 'galery'

class GaleryDetailView(DetailView):
    model = Galery
    template_name = 'galery/galery_detail.html'
    context_object_name = 'galery'

class GaleryCreateView(CreateView):
    model = Galery
    form_class = GaleryForm
    template_name = 'galery/galery_form.html'
    success_url = reverse_lazy('galery_list')

class GaleryUpdateView(UpdateView):
    model = Galery
    form_class = GaleryForm
    template_name = 'galery/galery_form.html'
    success_url = reverse_lazy('galery_list')
    
class GaleryDeleteView(DeleteView):
    model = Galery
    template_name = 'galery/galery_delete.html'
    context_object_name = 'galery'
    success_url = reverse_lazy('galery_list')


def login_user(request):
    if request.method == 'POST':
        form = LoginForm(data=request.POST)
        if form.is_valid():
            login(request, form.get_user())
            if request.GET.get('next'):
                return redirect(request.GET.get('next'))
            return redirect('index_render')
    else:
        form = LoginForm()
    context = {
        'form': form
    }
        
    
    return render(request, 'auth/login.html', context)


def registration_user(request):
    if request.method == 'POST':
        form = RegistrationForm(data=request.POST)
        if form.is_valid():
            login(request, form.save())
            if request.GET.get('next'):
                return redirect(request.GET.get('next'))
            return redirect('index_render')
    else:
        form = RegistrationForm()
    context = {
        'form': form
    }
    return render(request, 'auth/registration.html', context)


def logout_user(request):
    logout(request)
    return redirect('index_render')