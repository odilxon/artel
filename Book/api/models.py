from django.db import models
from datetime import datetime
from django.contrib.auth.models import User
# Create your models here.



class Book(models.Model):
    title = models.CharField(max_length=256)
    authors = models.CharField(max_length=500)
    price = models.FloatField()
    release_date = models.DateField()

class Order(models.Model):
    customer = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateTimeField(default=datetime.now, blank=True)
    status = models.CharField(max_length=100, blank=True)
    shipping_address = models.CharField(max_length=256)

class Ordermeta(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    count = models.IntegerField()


