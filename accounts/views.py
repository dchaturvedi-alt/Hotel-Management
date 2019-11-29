from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.models import User,auth
from django.contrib import messages
from booking.models import *
from django.utils.dateparse import parse_date
from django.shortcuts import render, redirect
import time
from django.contrib.auth.models import User, auth
from django.http import HttpResponse
# Create your views here.
import datetime
from django.utils.dateparse import parse_date
from website.models import *
from .models import *
from django.contrib import messages
from .models import *
from random import randint
import smtplib
from django.core.mail import send_mail
from django.conf import settings
# import config

def register(request):
    if(request.method=='POST'):

        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username=request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['confirm_password']
        if(len(password)<8):
            messages.info(request,"Password's minimum length should be 8")
            return redirect('/accounts/register')
        if(password2==password):
            if(User.objects.filter(username=username).exists()):
                messages.info(request,'Username Taken')
                print("hello1")
                return redirect('/accounts/register')
            elif(User.objects.filter(email=email).exists()):
                messages.info(request,'Email Already Registered')
                print("hello2")
                return redirect('/accounts/register')
            else:
                # print("hello3")
                user = User.objects.create_user(username=username, password=password, email=email, first_name=first_name, last_name=last_name)
                user.is_active = False
                user.code=randint(1000,9999)
                v = verified()
                v.user=email
                v.code=user.code

                v.save()
                user.save()
                subject = 'Thank you for registering to our site'
                message = str(user.code)
                email_from = settings.EMAIL_HOST_USER
                recipient_list = [email,]
                send_mail(subject, message, email_from, recipient_list)
                return render(request,'verify.html',{'email':email})
                # return redirect('/accounts/login')

        else:
            print("hello4")
            messages.info(request,'password not matching')
            return redirect('/accounts/register')

        return redirect('/')
    return render(request,'register.html')

def login(request):
    # print("i")
    try:
        if(request.method=='POST'):
            print("laskdfj;lasdjfl;kasdj")
            
            username = request.POST['username']
            password = request.POST['password']
            user= auth.authenticate(username=username,password=password)
            if user is not None:
                print("login successful")
                print(user.is_active)
                auth.login(request,user)
                return redirect('/')   
            else:
                print("login failed")
                messages.info(request,'Invalid Credentials')
                return redirect('/accounts/login')
        else:
            print("uder nhi  to idher   ")
            return render(request,'login.html')
    except:
        return render(request,'login.html')
    
    # return HttpResponse("hello world")
def logout(request):
    
    auth.logout(request)
    return redirect('/')
def profile(request):
    user=request.user
    z=user.booking_set.all()
    # for i in messages:
        # print(i)
    
    return render(request,'profilesave.html',{'bookings' : z})
    

def cancel(request):
    user = request.user
    print("idhhheeerr aaya")
    z = user.booking_set.all()
    if(request.method == "GET"):
        flag = False
        return render(request, 'cancel.html', {'flag': flag, 'bookings': z})
    else:
        flag = True
        roomno = RoomNo.objects.filter(rno=request.POST['cancel'])[0]
        Booking.objects.get(RNo=roomno).delete()
        roomno.available = True
        roomno.save()
        # b.save()
        # print(roomno)
        # messages.success(request, "Congratulations, Cancellation Successful")
        return render(request, 'cancelsuccessful.html', {'flag': flag})
    return render(request, 'cancelsuccessful.html')


def verify(request):
    email=request.POST['email']
    otp=request.POST['otp']
    v = verified.objects.filter(user=email)[0]
    print("verify me to aa raha haix")
    user=User.objects.get(email=email)
    print(user, email, otp, v.code)
    if(str(otp)==str(v.code)):
        print("sa;dfjla;sjdflkjasdlkfja;lskjdf;lasjd;lfkjas;ldjf;lkasjdf")
        user.is_active=True
        user.save()
        print(user.is_active)
        v.delete()
        return redirect('login')
    messages.info(request,"Wrong Otp")
    user.delete()
    v.delete()
    # return redirect('accounts/register')
    # print(user,email,otp,v.code)
    # return HttpResponse("hola")
    return redirect('register')

