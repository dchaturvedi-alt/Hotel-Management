from django.shortcuts import render
from django.http import HttpResponse
from django.contrib import messages
from django.core.mail import send_mail
# Create your views here.
from .models import *
def home(request):
    flag=False
    print(request.method)
    # print(request.method)
    
    if(request.method=='POST'):
        flag=True
        print(1)
    # for message in messages:
    #     print(message)
    
    room=Rooms.objects.all()
    service=Service.objects.all()
    return render(request,'index.html',{'rooms':room,'services':service,'flag':flag})

def check_available(request):
    available = False
    allrooms=r.roomno_set.get()
    for i in allrooms:
        if(i.available):
            available=True
            break
def room(request):
    return render(request,'room.html')

def about(request):
    return render(request,'about.html')
def blog(request):
    return render(request,'blog.html')
    # return render(request,'verify.html')
def singleblog(request):
    return render(request,'single-blog.html')

def contact(request):
    return render(request,'contact.html')
