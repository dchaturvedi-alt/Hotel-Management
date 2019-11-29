
from django.shortcuts import render,redirect
import time
from django.contrib.auth.models import User, auth
from django.http import HttpResponse
# Create your views here.
import datetime
from django.utils.dateparse import parse_date
from website.models import *
from .models import *
from django.contrib import messages
from django.contrib.auth.decorators import login_required
# from accounts.urls import *
# @login_required
@login_required(login_url='http://127.0.0.1:8000/accounts/login')
def check_available(request):
    if(request.method == "POST"):
        available = False
        # print(Rooms.objects.get(id=request.POST['room']))
        r=Rooms.objects.get(id=request.POST['room'])
        R=Rooms.objects.all()
        # print(R)
        checkin = parse_date(request.POST['checkin-date'])
        checkout = parse_date(request.POST['checkout-date'])
        curdate = datetime.datetime.now().date()
        Condi=True
        if(checkin > checkout or curdate > checkin):
            messages.info(request, 'Invalid Date')
            return redirect('/')
            Condi=False
        allrooms = r.roomno_set.all()
        price=0
    
        for i in allrooms:
            # print(i.rno)
            
            if(i.available):
                available = True
                price=i.roomtype.cost
                rola=i.roomtype
                break
        # print(available)
        if(available==False):
            messages.info(request,'No rooms Available')
            return redirect('/')
        D = {'available': available, 'condition': Condi,
             'checkindate': request.POST['checkin-date'], 'checkoutdate': request.POST['checkout-date'], 'room': r, 'adults': request.POST['adults'],'price':price}
        print(D)
        return render(request, 'booksave.html',D)
    else:
        return redirect('/')


@login_required(login_url='http://127.0.0.1:8000/accounts/login')
def book(request):
    r = Rooms.objects.get(id=request.POST['room'])
    cur=r.roomno_set.all()
    # if (request.user.is_authenticated() is True):
    #     pass
    # else:
    #     return redirect('http://127.0.0.1:8000/accounts/login')
    for i in cur:
        if(i.available==True):
            i.available=False
            i.save()
            b=Booking()
            b.user=request.user
            b.RNo=i
            b.checkin = parse_date(request.POST['checkin-date'])
            b.checkout = parse_date(request.POST['checkout-date'])
            # print(b.checkin)
            # b.person=request.POST['adults']
            b.save()
            break
    # messages.success(request,"Congratulations, Booking Successful")
    # print("me idher aaaaaaaaaaaaaaaaaaaaaaaaaaayyyyyyyyyyyyyyyyyyyyyyyyyyyaaaaaaaaaaaaa")
    # return redirect('/accounts/profile')
    return render(request,'successful.html')


@login_required(login_url='http://127.0.0.1:8000/accounts/login')
def cancel(request):
    user = request.user
    z=user.booking_set.all()
    if(request.method=="GET"):
        flag=False
        return render(request,'cancel.html',{'flag':flag,'bookings' : z})
    else:
        flag=True
        roomno=RoomNo.objects.filter(rno=request.POST['cancel'])[0]
        Booking.objects.get(RNo=roomno).delete()
        roomno.available = True
        roomno.save()
        # b.save()
        # print(roomno)
        messages.success(request, "Congratulations, Cancellation Successful")
        return redirect('/accounts/profile')
        return render(request,'cancel.html',{'flag':flag})
    return render(request,'cancelsuccessful.html')

def payment(request):
    # return HttpResponse("1234")
    return render(request,'payment.html')
