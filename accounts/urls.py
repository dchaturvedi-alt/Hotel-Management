from django.urls import include, path
from . import views
urlpatterns = [
    path('register', views.register, name='register'),
    path('login',views.login,name='login'),
    path('verify',views.verify,name='verify'),
    path('logout',views.logout,name='logout'),
    path('profile',views.profile,name='profile'),
    path('cancel', views.cancel, name='cancel'),
]
