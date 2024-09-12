from django.urls import path
from . views import *

urlpatterns = [
    path('index1/',index),
    path('about1/',about),
     # Customer URLs
    path('customerlist/', customerlist, name='customer_list'),
    path('customeradd/', customeradd, name='cus_add'),
    path('customerupdate/<int:id>/', customerupdate, name='cus_update'),
    path('customerdelete/<int:id>/', customerdelete, name='cus_delete'),
    

]