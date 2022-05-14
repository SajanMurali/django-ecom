from cgi import print_exception
from unicodedata import name
from django.db import models
from django.contrib.auth.models import user


class Costumer(models.Model):
     user = models.OneToOneField(user,on_delete=models.CASCADE,null=True,blank=True)
     name = models.CharField(max_length=200,null=True)
     email = models.CharField(max_length=200,null=True)

def __str__(self):
    return self.name

class Products(models.Model):
    name =  models.CharField(max_length=200,null=True)
    price = models.FloatField()
    digital = models.BooleanField(default=False,null=True,blank=False)

def __str__(self):
    return self.name

class Order(models.Model):
    costumer=  models.ForeignKey(Product,on_delete=models.SET_NULL,null=True)
    order = models.ForeignKey(Order,on_delete=models.SET_NULL,null=True)
    digital = models.IntegerField(default=0,null=True,blank=False)
    date_added = models.IntegerField(auto_now_add=True)
# Create your models here.
