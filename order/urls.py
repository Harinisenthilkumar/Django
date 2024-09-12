from django.urls import path
from . views import *
from.models import *
from .forms import *

urlpatterns = [
    path('orderlist/', orderlist, name='order_list'),
    path('orderadd/',orderadd, name='odr_add'),
    path('orderupdate/<int:id>/', orderupdate, name='odr_update'),
    path('orderdelete/<int:id>/', orderdelete, name='odr_delete'),
    
    
]
