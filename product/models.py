from django.db import models

# Create your models here.
class Product(models.Model):
    Brand_name = models.CharField(max_length=200,null=True)
    
    model_name = models.CharField(max_length=200,null=True)
    
    price = models.IntegerField(default=0)
    
    gst = models.FloatField(default=0)
    
    final_price = models.FloatField(default=0)
    
    def __str__(self):
        return self.Brand_name+" "+self.model_name
    
   
#---------------------------------------------------------------------------------------------------------------------------------------------------
# --------------------------ORDER TABLE - ----------------------------------------------------------------------------------------------------------



    
