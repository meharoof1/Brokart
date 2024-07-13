from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from . models import Customers

# Create your views here.
def show_account(request):
    context={}
    if request.POST and 'register' in request.POST:
        context['register']=True
        try:
            username=request.POST.get('username')
            email=request.POST.get('email')
            password=request.POST.get('password')
            phone=request.POST.get('phone no')
            address=request.POST.get('address')
            # create a user account
            user=User.objects.create_user(
                username=username,
                email=email,
                password=password
            )
            # create a customer account
            customer=Customers.objects.create(
                name=username,
                user=user,
                phone=phone,
                address=address
            )
            succes_message="REGISTERED SUCCESSFULLY "
            messages.success(request,succes_message)
        except Exception as e:
            error_message="Duplicate username"
            messages.error(request,error_message)   
    if request.POST and 'login' in request.POST:
        context['register']=False
        username=request.POST.get('username')
        password=request.POST.get('password')
        user=authenticate(username=username,password=password)
        if user:
            login(request,user)
            return redirect('home')
        else:
            messages.error(request,"invalid user credentials")   
    return render(request,'account.html',context)
        
def sign_out(request):
    logout(request)
    return redirect('home')