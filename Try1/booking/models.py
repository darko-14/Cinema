from django.db import models
from django.utils import timezone


class Ticket(models.Model):     
    movie = models.CharField(max_length=100)
    date = models.CharField(max_length=100)
    price = models.PositiveSmallIntegerField(default=0)
    seats = models.CharField(max_length=10)
    num = models.PositiveSmallIntegerField(default=0)
    total= models.PositiveSmallIntegerField(default=0)
    email = models.EmailField(max_length = 254)
    name = models.CharField(max_length=100, default="")
    
    def __str__(self):
        return self.movie


