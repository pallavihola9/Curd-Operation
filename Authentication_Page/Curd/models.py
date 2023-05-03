from django.db import models

# Create your models here.
class Users(models.Model):
    srnumber= models.CharField(max_length=150)
    fname= models.CharField(max_length=100)
    lname= models.CharField(max_length=100)
    email= models.CharField(max_length=100)
    address= models.CharField(max_length=200)
    phonenumber= models.CharField(max_length=10)
