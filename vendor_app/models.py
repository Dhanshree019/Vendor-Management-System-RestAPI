from django.db import models

# Create your models here.
class VendorDetails(models.Model):
    name = models.CharField(max_length=200)
    contact_details = models.TextField(max_length=255)
    address = models.TextField(max_length=500)
    vendor_code = models.CharField(max_length=100)
    on_time_delivery_rate = models.FloatField()
    fulfillment_rate = models.FloatField()

    def __str__(self):
        return self.name
    
    class Meta:
        db_table = 'vendor_details'
        verbose_name = "vendor_details"
        

# class PurchaseOrder(models.Model):
#     po_number = models.CharField(max_length=100)
#     vendor = models.ForeignKey(VendorDetails,on_delete=models.CASCADE)
#     order_date = models.DateTimeField(auto_now_add=True)
#     delivery_date = models.DateTimeField(auto_now=True)


