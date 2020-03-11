from django.conf import settings
from django.db import models
from django.utils import timezone


class Customer(models.Model):
    name = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    birth_date = models.DateTimeField()

    def __str__(self):
        return self.name

class Car(models.Model):
    color = models.CharField(max_length=30)
    brand = models.CharField(max_length=30)
    purchase_date = models.DateTimeField()
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)

    def __str__(self):
        return self.color + ' ' + self.brand
