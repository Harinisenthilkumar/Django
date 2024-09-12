from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import *
from .forms import *
def index(request):
    return render(request,'index.html')
def about(request):
    return render(request,'about.html')

def customerlist(request):
    data={"cuslist":Customer.objects.all()}
    print(data)
    return render(request,'customerlist.html',data)

#---------------------------------------------------------------------------------------------------------------------------------------------------
def customeradd(request):
    data = {"cusform":CustomerForm}
    new_data = CustomerForm(request.POST)
    if new_data.is_valid():
        new_data.save()
        return redirect('/customer/customerlist/')
    return render(request,'customeradd.html',data)

#-------------------------------------------------------------------------------------------------------------------------------------------------
def customerdelete(request,id):
    selected_data = Customer.objects.get(id=id)
    selected_data.delete()
    return  redirect('/customer/customerlist/')

#-------------------------------------------------------------------------------------------------------------------------------------------------
def customerupdate(request,id):
    selected_data = Customer.objects.get(id=id)
    data = {"cusform":CustomerForm(instance=selected_data)}
    
    if request.method == 'POST':
        new_data = CustomerForm(request.POST,instance=selected_data)
        
        if new_data.is_valid():
            new_data.save()
            return redirect('/customer/customerlist/')
    return render(request,'customeradd.html',data)

    
