from cgi import print_exception
from itertools import product
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
    costumer=  models.ForeignKey(Costumer,on_delete=models.SET_NULL,null=True)
    date_ordered = models.DateTimeField(auto_now_add=True)
    complete = models.IntegerField(default=0,null=True,blank=False)
    transaction_id= models.CharField(max_length=200,null=True)


def __str__(self):
    return (self.id)
class OrderItem(models.Model):
    product=  models.ForeignKey(product,on_delete=models.SET_NULL,null=True)
    order = models.ForeignKey(Order,on_delete=models.SET_NULL,null=True)
    quantity = models.IntegerField(default=0,null=True,blank=True)
    date_added = models.DateTimeField(auto_now_add=True)

class ShippingAddress(models.model):
    costumer =  models.ForeignKey(Costumer,on_delete=models.SET_NULL,blank=True,null=True)
    order = models.ForeignKey(Order,on_delete=models.SET_NULL,blank=True,null=True)
    address=  models.CharField(max_length=200,null=True)
    city =  models.CharField(max_length=200,null=True)
    state =  models.CharField(max_length=200,null=True)
    zipcode =  models.CharField(max_length=200,null=True)
    date_added = models.DateTimeField(auto_now_add=True)


def __str__(self):
    return self.address
