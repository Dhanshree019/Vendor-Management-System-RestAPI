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
        

class PurchaseOrder(models.Model):
    po_number = models.CharField(max_length=100)
    vendor = models.ForeignKey(VendorDetails,on_delete=models.CASCADE)
    order_date = models.DateTimeField(auto_now_add=True)
    delivery_date = models.DateTimeField()
    items = models.JSONField()
    quantity = models.IntegerField()
    status = models.CharField(max_length=255)
    quality_rating = models.FloatField()
    issue_date = models.DateTimeField()
    acknowledgment_date = models.DateTimeField(null=True,blank=True)

    def __str__(self):
        return self.po_number
    
    class Meta:
        db_table = 'purchase_order'
        verbose_name = 'purchase_order'


class HistoricalPerformance(models.Model):
    vendor = models.ForeignKey(VendorDetails,on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)
    on_time_delivery_rate = models.FloatField()
    quality_rating_avg = models.FloatField()
    average_response_time = models.FloatField()
    fulfillment_rate = models.FloatField()

    def __str__(self):
        return self.vendor
    
    class Meta:
        db_table = 'historical_performance'
        verbose_name = 'historical_performance'




