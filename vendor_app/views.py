from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from .models import *
from .serializers import *

# Create your views here.
class VendorView(APIView):
    def post(self,request):
        try:
            vendor_data = request.data
            vendor = VendorSerializer(data=vendor_data)
            if vendor.is_valid():
                vendor.save()
                return Response({"message":"Vendor created successfully","vendor_id":vendor.data['id']},status=status.HTTP_201_CREATED)
            else:
                return Response({"message":"Vendor creation failed"},status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({"message":f"An unexpected error occurred : {str(e)}"},status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def get(self,request):
        try:
            vendor_id = request.GET.get('vendor_id')
            vendor_details = None
            if vendor_id:
                vendor_details = VendorDetails.objects.filter(id=vendor_id).first()
                if vendor_details is not None :
                    vendor_details = VendorSerializer(vendor_details).data              
            else:
                vendor_details = VendorDetails.objects.all()
                if len(vendor_details) > 0:
                    vendor_details = VendorSerializer(vendor_details,many=True).data
            if vendor_details:
                return Response({"message":"Data reterive successfully","data":vendor_details},status=status.HTTP_200_OK)
            else:
                return Response({"message":"Data not found"},status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return Response({"message":f"An unexpected error occurred - {str(e)}"},status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    
    def put(self,request):
        try:
            vendor_id = request.GET.get('vendor_id')
            if vendor_id:
                vendor_details = VendorDetails.objects.filter(id=vendor_id).first()
                vendor_serializer = VendorSerializer(instance=vendor_details,data=request.data,partial=True)
                if vendor_serializer.is_valid():
                    vendor_serializer.save()
                    return Response({"message":"Data updated successfully","data":vendor_serializer.data},status=status.HTTP_200_OK)
            else:
                return Response({"message":"Data not found"},status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return Response({"message": f"An unexpected exception occurred - {str(e)}"},status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def delete(self,request):
        try:
            vendor_id = request.GET.get('vendor_id')
            if vendor_id:
                vendor_details = VendorDetails.objects.filter(id=vendor_id)
                print(vendor_details)
                if vendor_details.exists():
                    vendor_details.delete()
                    return Response({"message":"Vendor deleted successfully"},status=status.HTTP_200_OK)
                else:
                    return Response({"message":"Vendor data not found"},status=status.HTTP_404_NOT_FOUND)
            else:
                return Response({"message":"Vendor id required"},status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({"message":f"An unexpected error occurred - {str(e)}"},status=status.HTTP_500_INTERNAL_SERVER_ERROR)

class PurchaseOrderView(APIView):
    def post(self,request):
        try:
            purchase_data = PurchaseOrderSerializer(data = request.data)
            if purchase_data.is_valid():
                purchase_data.save()
                return Response({"message":"Purchase data created successfully","po_id":(purchase_data.data)["id"]},status=status.HTTP_201_CREATED)
            else:
                return Response({"message": "Enter data is not valid","data":purchase_data.data},status=status.HTTP_400_BAD_REQUEST)

        except Exception as e:
             return Response({"message":f"An unexpected error occurred - {str(e)}"},status=status.HTTP_500_INTERNAL_SERVER_ERROR)   
        

            

            
            


        

