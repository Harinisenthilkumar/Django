from django.shortcuts import render,redirect

from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from.models import *
from django.views import View as view

class AuthLoginPageView(view):
    def get(self, request):
        return render(request, 'loginpage.html')
    
    def post(self, request):
        print(request.POST)
        user_data=authenticate(username=request.POST['username'],password=request.POST['password'])
        print(user_data)
        
        if user_data is not None:
            login(request,user_data)
            return redirect('/product/productlist/')
        else:
            msg={"error":"Invalid username or password"}
            return render(request,'loginpage.html',msg)
#-------------------------------------------------------------------------------------------------------------------------------------------------
class AuthLogoutPageView(view):
    def get(self, request):
        logout(request)
        return redirect('/')
 #--------------------------------------------------------------------------------------------------------------------------------------------------
class AuthSignupPageView(view):
    def get(self, request):
        return render(request, 'Signup.html')
    
    def post(self, request):
         user_check = User_details.objects.filter(username=request.POST['username']) 
         print(user_check) 
         if len(user_check)>0: 
             msg = {"error": "Username already exists"} 
             return render(request,"Signup.html",msg) 
         else:         
            new_user = User_details(
            username = request.POST['username'],
            password = request.POST['password'],
            first_name = request.POST['first_name'],
            last_name = request.POST['last_name'],
            Mobile_number = request.POST['phone'],
            Age = request.POST['age'],
            Address = request.POST['address']
            )
            new_user.set_password(request.POST['password'])
            new_user.save()
            return redirect('/login/')
            return render(request ,'Signup.html')
        
        




