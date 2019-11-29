from django.db import models

# Create your models here.

class Rooms(models.Model):
    name = models.CharField(max_length=100)
    cost = models.IntegerField()
    size = models.IntegerField()
    person = models.IntegerField()
    bed = models.CharField(max_length=50)     
    wifi = models.BooleanField(default=False)
    tv= models.BooleanField(default=False)      
    img= models.ImageField(upload_to='pics') 
    ac= models.BooleanField(default=False)
    tv=models.BooleanField(default=False)
    def __str__(self):
        return self.name

class Service(models.Model):
    name =models.CharField(max_length=50)
    img = models.ImageField(upload_to='pics')
    def __str__(self):
        return self.name

class Event(models.Model):
    date=models.DateField(auto_now=False, auto_now_add=False)
    time=models.TimeField(auto_now=False, auto_now_add=False)
    desc=models.TextField()
    link=models.CharField(max_length=200)
    img=models.ImageField(upload_to='pics/Event')

class RoomNo(models.Model):
    roomtype=models.ForeignKey(Rooms,on_delete=models.CASCADE)
    rno=models.IntegerField()
    available=models.BooleanField(default=True)
    def __str__(self):
        return str(self.rno)


