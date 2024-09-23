from django import forms
from .models import *
 

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = '__all__'
        
        widgets = {" Brand_name":forms.TextInput(attrs={"class":"form-control","placeholder":"Brand Name"}),
                  "model_name":forms.TextInput(attrs={"class":"form-control","placeholder":"Model Name"}),
                  "price":forms.NumberInput(attrs={"class":"form-control","placeholder":"Price"}),
                  "gst":forms.NumberInput(attrs={"class":"form-control","placeholder":"GST"}),
                  "final_price":forms.NumberInput(attrs={"class":"form-control","placeholder":"Final Price"}),
                  "picture":forms.FileInput(attrs={"class":"form-control"}),          
        }
