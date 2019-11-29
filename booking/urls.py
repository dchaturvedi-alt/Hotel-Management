from django.urls import include, path
from . import views
from django.contrib import admin

urlpatterns = [
    path('', views.check_available, name='check_available'),
    path('success',views.book,name='book'),
    path('cancel',views.cancel,name='cancel'),
    path('payment',views.payment,name='payment')

]
