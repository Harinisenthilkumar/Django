from django.shortcuts import render,redirect

from django.http import HttpResponse
from .models import *
from .forms import *
from django.views import View
def index(request):
    data={ "user1":[
        {'name':'harini','location':'madurai','score':90},
        {'name':'shanmu','location':'chennai','score':80},
        {'name':'shree','location':'madurai','score':89},
        {'name':'dk','location':'madurai','score':70}
    ]
    }

    return render(request,'home.html',data)

def about(request):
    return render(request,'about.html')

#-------------------------------------------------
class ProductListView(View):
    def get(self,request):
        data = {"prolist":Product.objects.all()}
        print(data)
        return render(request,'productlist.html',data)


#---------------------------------------------------------------------------------------------------------------------------------------------------
class ProductAddView(View):
    def get(self,request):
        data = {"proform":ProductForm()}
        return render(request,'productadd.html',data)
    
    def post(self,request):
        new_data = ProductForm(request.POST,request.FILES)
        if new_data.is_valid():
            new_data.save()
            return redirect('/product/productlist/')
        
        
#-------------------------------------------------------------------------------------------------------------------------------------------------
class ProductDeleteView(View):
    def get (self,request,id):
        selected_data = Product.objects.get(id=id)
        selected_data.delete()
        return  redirect('/product/productlist/')

#----------------------------------------------------------------------------------------------------------------------------------------------

class ProductUpdateView(View):
    def get(self,request,id):
        selected_data = Product.objects.get(id=id)
        data = {"proform":ProductForm(instance=selected_data)}
        return render(request,'productadd.html',data)
    
    def post(self,request,id):
        selected_data = Product.objects.get(id=id)
        new_data = ProductForm(request.POST,instance=selected_data)
        if new_data.is_valid():
            new_data.save()
            return redirect('/product/productlist/')
    
        
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    

    
    
    
    
    
    
    
    
    
    

