from django import forms
from.models import *

# class ClothForm(forms.ModelForm):
#     class Meta:
#         model = Cloth
#         fields =['name','description', 'price','color', 'min_size', 'max_size', 'photo', 'is_exists', 'collection', 'category']


class BicycleForm(forms.ModelForm):
    class Meta:
        model = Bicycle
        fields =['name','price','brend', 'is_exists']


class PhotoBicycleForm(forms.ModelForm):
    class Meta:
        model = PhotoBicycle
        fields =['bicycle', 'photo']

class ClientsForm(forms.ModelForm):
    class Meta:
        model = Clients
        fields =['clint_name', 'email', 'phone']


class OrdersForm(forms.ModelForm):
    class Meta:
        model = Orders
        fields =['status']

class OrderDetailForm(forms.ModelForm):
    class Meta:
        model = OrderDetail
        fields =['count', 'price_for_count']

class EmployeeForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields =['employee_name', 'status', 'employee_phone']

class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields =['rating', 'comment']

class GaleryForm(forms.ModelForm):
    class Meta:
        model = Galery
        fields =['name', 'comment', 'photo']


