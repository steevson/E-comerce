from django.db import models
from datetime import datetime, timedelta

from django.urls import reverse


# Create your models here.
class categ (models.Model):
    name = models.CharField(max_length=200,unique=True)
    slug = models.SlugField(max_length=200, unique=True)

    def __str__(self):
        return '{}'.format(self.name)
    def get_url(self):
        return reverse('product_cate',args=[self.slug])


class product (models.Model):
    img = models.ImageField(upload_to='picture')
    name = models.CharField(max_length=50)
    slug = models.SlugField(max_length=200, unique=True)
    price = models.PositiveIntegerField()
    Description = models.TextField()
    availability = models.BooleanField(default=True)
    stock = models.PositiveIntegerField()
    category = models.ForeignKey(categ, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return '{}'.format(self.name)
    def get_url(self):
        return reverse('details',args=[self.category.slug ,self.slug])