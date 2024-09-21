from django.urls import path
from .views import *

urlpatterns = [
    path('',AuthLoginPageView.as_view()),
    path('logout/',AuthLogoutPageView.as_view()),
    path('signup/',AuthSignupPageView.as_view()),
]
