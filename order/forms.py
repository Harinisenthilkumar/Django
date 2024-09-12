
from django import forms
from .models import *
 

class orderForm(forms.ModelForm):
    class Meta:
        model = order
        fields =['product_ref','customer_ref','order_date','quality']
