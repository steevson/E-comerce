from django.db import models
from home.models import *
from django.contrib.auth.models import User
# Create your models here.

class cartlist(models.Model):
    cart_id = models.CharField(max_length=250,unique=True)
    date_added = models.DateTimeField(auto_now_add=True)
    user =models.ForeignKey(User, on_delete=models.CASCADE, null=True, default=None)
    def __str__(self):
        return self.cart_id
class items(models.Model):
    prod = models.ForeignKey(product,on_delete=models.CASCADE)
    cart = models.ForeignKey(cartlist,on_delete=models.CASCADE)
    quan = models.IntegerField()
    active =models.BooleanField(default=True)
    def __str__(self):
        return str(self.prod)
    def total(self):
        return self.prod.price*self.quan


class billing(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    cart = models.ForeignKey(cartlist, on_delete=models.CASCADE, null=True)
    firstname = models.CharField(max_length=50)
    lastname = models.CharField(max_length=50)
    country = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    address = models.TextField()
    town = models.CharField(max_length=50)
    postcode = models.BigIntegerField()
    phone = models.BigIntegerField()
    email = models.CharField(max_length=150)


class bankform(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    firstname = models.CharField(max_length=50)
    lastname = models.CharField(max_length=50)
    accountno = models.BigIntegerField()
    cvv = models.PositiveIntegerField()
    expiryFrom = models.DateTimeField()
    upto = models.DateTimeField()

