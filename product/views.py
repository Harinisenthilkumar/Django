from django.shortcuts import render,redirect

from django.http import HttpResponse
from .models import *
from .forms import *
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
def productlist(request):
    data={"prolist":Product.objects.all()}
    print(data)
    return render(request,'productlist.html',data)



#---------------------------------------------------------------------------------------------------------------------------------------------------
def productadd(request):
    data = {"proform":ProductForm}
    new_data = ProductForm(request.POST)
    if new_data.is_valid():
        new_data.save()
        return redirect('/product/productlist/')
    return render(request,'productadd.html',data)

#-------------------------------------------------------------------------------------------------------------------------------------------------

def productdelete(request,id):
    selected_data = Product.objects.get(id=id)
    selected_data.delete()
    return  redirect('/product/productlist/')
#----------------------------------------------------------------------------------------------------------------------------------------------

def productupdate(request,id):
    selected_data = Product.objects.get(id=id)
    data = {"proform":ProductForm(instance=selected_data)}
    
    if request.method == 'POST':
        new_data = ProductForm(request.POST,instance=selected_data)
        
        if new_data.is_valid():
            new_data.save()
            return redirect('/product/productlist/')
    return render(request,'productadd.html',data)
    
    
    
    
    
    
    
    
    
    
    
    

