from django.shortcuts import render
from .serializers import *
from rest_framework import viewsets
from rest_framework.permissions import IsAdminUser

from shop.models import *
from .permission import *
# Create your views here.

class BicycleViewSet(viewsets.ModelViewSet):
    queryset = Bicycle.objects.all()
    serializer_class = BicycleSerializer
    permission_classes = [IsAdminUser]
    pagination_class = PaginationPage


class PhotoBicycleViewSet(viewsets.ModelViewSet):
    queryset = PhotoBicycle.objects.all()
    serializer_class = PhotoBicycleSerializer
    permission_classes = [IsAdminUser]
    pagination_class = PaginationPage

class ClientsViewSet(viewsets.ModelViewSet):
    queryset = Clients.objects.all()
    serializer_class = IsAdminUser
    permission_classes = [IsAdminUser]
    pagination_class = PaginationPage

class OrdersViewSet(viewsets.ModelViewSet):
    queryset = Orders.objects.all()
    serializer_class = OrdersSerializer
    permission_classes = [IsAdminUser]
    pagination_class = PaginationPage

class OrderDetailViewSet(viewsets.ModelViewSet):
    queryset = OrderDetail.objects.all()
    serializer_class = OrderDetailSerializer
    permission_classes = [IsAdminUser]
    pagination_class = PaginationPage

class EmployeeViewSet(viewsets.ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
    permission_classes = [CustomPermissions]
    pagination_class = PaginationPage

class ReviewViewSet(viewsets.ModelViewSet):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    permission_classes = [CustomPermissionsWithoutDeletePut]
    pagination_class = PaginationPage

class GaleryViewSet(viewsets.ModelViewSet):
    queryset = Galery.objects.all()
    serializer_class = GalerySerializer
    permission_classes = [CustomPermissions]
    pagination_class = PaginationPage

class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    permission_classes = [CustomPermissions]
    pagination_class = PaginationPage

class Pos_orderViewSet(viewsets.ModelViewSet):
    queryset = Pos_order.objects.all()
    serializer_class = Pos_orderSerializer
    permission_classes = [CustomPermissions]
    pagination_class = PaginationPage