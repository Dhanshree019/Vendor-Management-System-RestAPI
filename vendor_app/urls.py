from django.urls import path
from .views import *
urlpatterns = [
path('vendors',VendorView.as_view()),
path('vendors/purchase_orders',PurchaseOrderView.as_view())
]