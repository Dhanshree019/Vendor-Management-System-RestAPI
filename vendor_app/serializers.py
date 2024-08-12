from rest_framework.serializers import ModelSerializer
from .models import VendorDetails

class VendorSerializer(ModelSerializer):
    class Meta:
        model = VendorDetails
        fields ='__all__'