from django.shortcuts import render ,redirect
from django.http import HttpResponse
from .models import *
from .forms import *

# Create your views here.

def orderlist(request):
    data={"odrlist":order.objects.all()}
    print(data)
    return render(request,'orderlist.html',data)

#---------------------------------------------------------------------------------------------------------------------------------------------------
def orderadd(request):
    data = {"odrform":orderForm}
    
    if request.method == 'POST':
        sp=Product.objects.get(id = request.POST['product_ref'])
        pro_price=float(request.POST['quality'])*sp.price
        pro_gst=(pro_price*sp.gst)/100
        pro_Fp =pro_price+pro_gst
        
        new_order =order(product_ref_id = request.POST['product_ref'],
                         customer_ref_id = request.POST['customer_ref'],
                         order_date =request.POST['order_date'],
                         quality = request.POST['quality'],
                         price =  pro_price,
                         gst = pro_gst,
                         final_price= pro_Fp,
                         )
        new_order.save()
        
        
        
        return redirect('/order/orderlist/')
    return render(request,'orderadd.html',data)

def orderdelete(request,id):
    selected_data = order.objects.get(id=id)
    selected_data.delete()
    return  redirect('/order/orderlist/')

#-------------------------------------------------------------------------------------------------------------------------------------------------
def orderupdate(request, id):
    selected_data = order.objects.get(id=id)
    data = {"odrform": orderForm(instance=selected_data)}
    
    if request.method == 'POST':
        sp = Product.objects.get(id=request.POST['product_ref'])
        pro_price = float(request.POST['quality']) * sp.price
        pro_gst = (pro_price * sp.gst) / 100
        pro_Fp = pro_price + pro_gst

        updated_row=order.objects.filter(id=id)
        updated_row.update(product_ref_id=request.POST['product_ref'],
                           customer_ref_id=request.POST['customer_ref'],
                           order_date=request.POST['order_date'],
                           quality=request.POST['quality'],
                           price=pro_price,
                           gst=pro_gst,
                           final_price=pro_Fp)
        return redirect('/order/orderlist/')
    
    return render(request, 'orderadd.html', data)

    



