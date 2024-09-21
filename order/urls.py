from django.urls import path
from . views import *
from.models import *
from .forms import *

urlpatterns = [
    path('orderlist/', OrderListview.as_view(), name='odr_list'),
    path('orderadd/', OrderAddview.as_view(), name='odr_add'),
    path('orderadd/<int:id>/', OrderUpdateView.as_view(), name='odr_update'),
    path('orderdelete/<int:id>/', OrderDeleteView.as_view(), name='odr_delete'),
    
    
    
    
]
