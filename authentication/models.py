from django.db import models
from django.contrib.auth.models import AbstractUser

class User_details(AbstractUser):
    Mobile_number = models.CharField(max_length=200)
    Address = models.CharField(max_length=200)
    Age = models.IntegerField(default=1)
    
    
    
    
    
    
    
    

# from product.models import *

# class Userdetails(models.Model):
#     First_name = models.CharField(max_length=200,null=True)

#     middle_name = models.CharField(max_length=200,null=True)

#     last_name = models.CharField(max_length=200,null=True)

#     Address = models.CharField(max_length=200,null=True)

#     phone_no = models.IntegerField(default=0)

#     Product_ref = models.ForeignKey(Product,on_delete=models.SET_NULL,null=True)

#     def __str__(self):
#         return self.name

