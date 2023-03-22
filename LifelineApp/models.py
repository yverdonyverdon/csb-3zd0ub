from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Signup(models.Model):
    firstname = models.CharField(max_length=50,null=True,blank=True)
    lastname = models.CharField(max_length=50,null=True,blank=True)
    username = models.CharField(max_length=50,null=True,blank=True)
    email = models.EmailField(max_length=50,null=True,blank=True)
    phoneno = models.IntegerField(null=True,blank=True)
    password =models.CharField(max_length =50,null=True,blank=True)

    def __str__(self):
        return str(self.username)