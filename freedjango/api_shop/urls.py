from .views import *
from rest_framework import routers

urlpatterns = [

]

router = routers.SimpleRouter()
router.register('bicycle', BicycleViewSet, basename='bicycle')
router.register('photobicycle', PhotoBicycleViewSet, basename='photobicycle')
router.register('clients', ClientsViewSet, basename='clients')
router.register('orders', OrdersViewSet, basename='orders')
router.register('orderdetail', OrderDetailViewSet, basename='orderdetail')
router.register('employee', EmployeeViewSet, basename='employee')
router.register('review', ReviewViewSet, basename='review')
router.register('galery', GaleryViewSet, basename='galery')
router.register('order', OrderViewSet, basename='order')
router.register('pos_order', Pos_orderViewSet, basename='pos_order')
urlpatterns += router.urls