from django.urls import path
from . views import *

urlpatterns = [
    path('index1/',index),
    path('about1/',about),
     # Customer URLs
   path('customerlist/',CustomerListView.as_view(),name='cus_list'),
   path('customeradd/',CustomerAddView.as_view(),name='cus_add'),
   path('customerupdate/<int:id>/',CustomerUpdateView.as_view(),name='cus_update'),
   path('customerdelete/<int:id>/', CustomerDeleteView.as_view(), name='cus_delete')

   
] 
