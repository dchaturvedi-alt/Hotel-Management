from django.db import models
from django.contrib.auth.models import User, auth
# Create your models here.
class verified(models.Model):
    # user = models.ForeignKey(User, on_delete="CASCADE")
    user=models.CharField(max_length=100)
    code=models.IntegerField()
