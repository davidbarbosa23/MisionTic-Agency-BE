from django.db import models


class Pack(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    is_active = models.BooleanField(default=True)
    discount = models.SmallIntegerField(default=0)
    country = models.CharField(max_length=50)
    image_url = models.CharField(
        max_length=255, default='https://cdn.pixabay.com/photo/2017/01/05/16/57/girl-1955797_960_720.jpg')
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
