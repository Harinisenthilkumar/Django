from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import *
from .forms import *
from django.views import View
def index(request):
    return render(request,'index.html')
def about(request):
    return render(request,'about.html')

class CustomerListView(View):
    def get(self,request):
        data = {"cuslist":Customer.objects.all()}
        print(data)
        return render(request,'customerlist.html',data)

class CustomerAddView(View):
    def get(self,request):
        data = {"cusform":CustomerForm}
        return render(request,'customeradd.html',data)
    
    def post(self,request):
        new_data = CustomerForm(request.POST)
        if new_data.is_valid():
            new_data.save()
            return redirect('/customer/customerlist/')

#---------------------------------------------------------------------------------------------------------------------------------------------------
def customeradd(request):
    data = {"cusform":CustomerForm}
    new_data = CustomerForm(request.POST)
    if new_data.is_valid():
        new_data.save()
        return redirect('/customer/customerlist/')
    return render(request,'customeradd.html',data)

#-------------------------------------------------------------------------------------------------------------------------------------------------
class CustomerDeleteView(View):
    def get(self, request, id):
        selected_data = Customer.objects.get(id=id)
        selected_data.delete()
        return redirect('/customer/customerlist/')
    

#-------------------------------------------------------------------------------------------------------------------------------------------------
class CustomerUpdateView(View):
    def get(self, request, id):
        selected_data = Customer.objects.get(id=id)
        data = {"cusform": CustomerForm(instance=selected_data)}
        return render(request,'customeradd.html', data)
    
    def post(self, request, id):
        selected_data = Customer.objects.get(id=id)
        new_data = CustomerForm(request.POST, instance=selected_data)
        if new_data.is_valid():
            new_data.save()
            return redirect('/customer/customerlist/')
  