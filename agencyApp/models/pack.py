from django.db import models


class Pack(models.Model):
    id = models.BigAutoField(primary_key=True)
    title = models.CharField(max_length=50)
    description = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    isActive = models.BooleanField(default=True)
    discount = models.SmallIntegerField(default=0)
    country = models.CharField(max_length=50)
    createdAt = models.DateTimeField(auto_now_add=True)
    modifiedAt = models.DateTimeField(auto_now=True)
