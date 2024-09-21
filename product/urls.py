from django.urls import path
from .views import *

urlpatterns = [
    path('home/',index),
    path('about1/',about),
    path('productlist/',ProductListView.as_view()),
    path('productadd/',ProductAddView.as_view()),
    
    path('productupdate/<int:id>/',ProductUpdateView.as_view(),name='pro_update'),
    path('productdelete/<int:id>/',ProductDeleteView.as_view(),name='pro_delete'),
    
]