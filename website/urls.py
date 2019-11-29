from django.urls import include, path
from . import views
from django.contrib import admin

urlpatterns = [
    path('', views.home, name='home'),
    path('room', views.room, name='home'),
    path('about',views.about,name='about'),
    path('blog',views.blog,name='blog'),
    path('singleblog',views.singleblog,name='singleblog'),
    path('contact',views.contact,name='contact'),

]
