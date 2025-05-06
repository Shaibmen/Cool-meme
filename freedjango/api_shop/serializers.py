from rest_framework import serializers
from shop.models import *

class BicycleSerializer(serializers.ModelSerializer):
    price = serializers.DecimalField(label='Цена', max_digits=10, decimal_places=2)
    class Meta:
        model = Bicycle
        fields = [
            'name',
            'price',
            'brend',
            'is_exists'
        ]

class PhotoBicycleSerializer(serializers.ModelSerializer):
    class Meta:
        model = PhotoBicycle
        fields = [
            'bicycle',
            'photo'
        ]

class ClientsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Clients
        fields = [
            'clint_name',
            'email',
            'phone'
        ]

class OrdersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Orders
        fields = [
            'client',
            'date',
            'status'
        ]

class OrderDetailSerializer(serializers.ModelSerializer):
    price_for_count = serializers.DecimalField(label='Цена за штуку', max_digits=10, decimal_places=2)
    class Meta: 
        model = OrderDetail
        fields = [
            'client',
            'order',
            'count',
            'price_for_count'
        ]

class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = [
            'employee_name',
            'status',
            'employee_phone'
        ]

class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = [
            'bicycle',
            'client',
            'rating',
            'comment'
        ]

class GalerySerializer(serializers.ModelSerializer):
    class Meta:
        model = Galery
        fields = [
            'name',
            'comment',
            'photo'
        ]


class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = [
            'SHOP',
            'COURIER',
            'PICKUPPOINT',
            'TYPE_DELIVERY',
            'buyer_firstname',
            'buyer_secondname',
            'buyer_surname',
            'comment',
            'delivery_address',
            'delivery_type',
            'date_create',
            'date_finish',
            'bicycle'
        ]

class Pos_orderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pos_order
        fields = [
            'bicycle',
            'order',
            'count',
            'discount'
        ]

