from django.db import models
from .user import User
from .pack import Pack


class Purchase(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    pack = models.ForeignKey(Pack, on_delete=models.CASCADE)
    total = models.DecimalField(max_digits=10, decimal_places=2)
    buyerID = models.IntegerField(default=1)
    buyerCard = models.IntegerField(default=1111111111111111)
    buyerCardName = models.CharField(max_length=50)
    buyerCardDueDate = models.DateField()
    buyerCardCVV = models.IntegerField(default=111)
    createdAt = models.DateTimeField(auto_now_add=True)
