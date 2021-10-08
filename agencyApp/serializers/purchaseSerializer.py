from rest_framework import serializers
from agencyApp.models.purchase import Purchase

class PurchaseSerializer(serializers.ModelSerializer):
    class Meta:
     model = Purchase
     fields = ['id','user', 'pack','total','buyerCard','buyerCardNam','buyerCardDueDate', 'buyerCardCVV', 'createdAt' ]

    def create(self, validated_data):
     
      purchaseInstance = Purchase.objects.create(**validated_data)
      return purchaseInstance


    def to_representation(self, obj):
           
           purchase = Purchase.objects.get(id=obj.id)       
           return {
                        'id': purchase.id, 
                        'user': purchase.PurchaseOrderID,
                        'pack': purchase.pack,
                        'total': purchase.total,
                        'buyerCard': purchase.buyerCard,
                        'buyerCardNam': purchase.buyerCardNam,
                        'buyerCardDueDate': purchase.buyerCardDueDate,
                        'buyerCardCVV': purchase.buyerCardCVV,
                        'createdAt': purchase.createdAt
                    }

            