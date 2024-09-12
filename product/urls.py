from django.urls import path
from .views import *

urlpatterns = [
    path('home/',index),
    path('about1/',about),
    path('productlist/',productlist),
    path('productadd/',productadd),
    path('productupdate/<int:id>/',productupdate,name='pro_update'),
    path('productdelete/<int:id>/',productdelete,name='pro_delete'),
    
    
]