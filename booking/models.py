from django.db import models
from website.models import *
from django.utils import timezone
from django.contrib.auth.models import User, auth
class Booking(models.Model):
    user=models.ForeignKey(User,on_delete="CASCADE")
    checkin=models.DateField()
    checkout=models.DateField()
    RNo=models.ForeignKey(RoomNo,on_delete="CASCADE")
    # people=models.IntegerField()

