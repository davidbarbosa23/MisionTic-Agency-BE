from rest_framework import generics
from agencyApp.models.purchase import Purchase
from agencyApp.serializers.purchaseSerializer import PurchaseSerializer


class PurchaseGetListView(generics.ListCreateAPIView):
    queryset = Purchase.objects.all()
    serializer_class = PurchaseSerializer
