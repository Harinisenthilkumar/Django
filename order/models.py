from django.db import models
from product.models import *
from customer.models import *



# Create your models here.

# Create your models here.
class order(models.Model):
    product_ref = models.ForeignKey('product.product',on_delete=models.SET_NULL,null=True)
    customer_ref = models.ForeignKey('customer.customer',on_delete=models.CASCADE,null=True)
    order_date = models.DateField(null=True)
    quality = models.IntegerField(default=0)
    price = models.IntegerField(default=0)
    gst = models.FloatField(default=0)
    final_price = models.FloatField(default=0)
    
  

    