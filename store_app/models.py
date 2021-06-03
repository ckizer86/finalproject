from django.db import models
from time import gmtime, localtime, strftime
from datetime import date, datetime
import re

# Create your models here.

class User(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    level = models.IntegerField(max_length=1, default=1)
    dob = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    #useraddress
    #userorders
    #userlike

class Address(models.Model):
    address_1 = models.CharField(max_length=255)
    address_2 = models.CharField(max_length=255, default="")
    city = models.CharField(max_length=255)
    state = models.CharField(max_length=255)
    zip = models.IntegerField(max_length=5)
    user = models.ForeignKey(User, related_name="useraddress", on_delete = models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    #shippingaddress

class Product(models.Model):
    name = models.CharField(max_length=255)
    desc = models.TextField()
    amount = models.IntegerField(max_length=25)
    pic = models.ImageField(upload_to='images/')
    likes = models.ManyToManyField(User, related_name="userlike")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    #categories
    #orders

class Category(models.Model):
    name = models.CharField(max_length=255)
    product = models.ManyToManyField(Product, related_name="categories")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Order(models.Model):
    product = models.ForeignKey(Product, related_name="orders", on_delete = models.CASCADE)
    user = models.ForeignKey(User, related_name="userorders", on_delete = models.CASCADE)
    tracking = models.CharField(max_length=255, default="")
    total = models.IntegerField(max_length=25)
    address = models.ForeignKey(Address, related_name="shippingaddress", on_delete = models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
class Store(models.Model):
    name = models.CharField(max_length=255)
    address_1 = models.CharField(max_length=255)
    address_2 = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    state = models.CharField(max_length=255)
    zip = models.IntegerField(max_length=5)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)