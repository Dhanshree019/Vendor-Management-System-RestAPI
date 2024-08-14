from rest_framework.serializers import ModelSerializer
from .models import *

class VendorSerializer(ModelSerializer):
    class Meta:
        model = VendorDetails
        fields ='__all__'

class PurchaseOrderSerializer(ModelSerializer):
    class Meta:
        model = PurchaseOrder
        fields ='__all__'