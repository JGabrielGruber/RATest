from django.db import models
from django.urls import reverse

# Create your models here.

class Product(models.Model) :
    name        = models.CharField(max_length=120)
    description = models.TextField()
    price       = models.DecimalField(max_digits=10, decimal_places=2, default="0.00")
    updated     = models.DateTimeField(auto_now=True, auto_now_add=False)
    timestamp   = models.DateTimeField(auto_now=False, auto_now_add=True)

    def __unicode__(self):
        return self.name

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('products:detail', kwargs={'id': self.id})
