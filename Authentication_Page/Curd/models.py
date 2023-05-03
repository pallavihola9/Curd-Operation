from django.db import models

# Create your models here.
class Users(models.Model):
    srnumber= models.CharField(max_length=50)
    fname= models.CharField(max_length=50)
    lname= models.CharField(max_length=50)
    email= models.CharField(max_length=100)
    address= models.CharField(max_length=200)
    phonenumber= models.CharField(max_length=10)
