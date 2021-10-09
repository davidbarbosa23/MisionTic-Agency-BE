from rest_framework import serializers
from agencyApp.models.purchase import Purchase


class PurchaseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Purchase
        fields = ['id', 'user', 'pack', 'total', 'buyerCard',
                  'buyerCardName', 'buyerCardDueDate', 'buyerCardCVV', 'createdAt']

    def create(self, validated_data):
        purchaseInstance = Purchase.objects.create(**validated_data)
        return purchaseInstance

    def to_representation(self, obj):
        purchase = Purchase.objects.get(id=obj.id)
        print(purchase)
        return {
            'id': purchase.id,
            'user': {
                'id': purchase.user.id,
                'first_name': purchase.user.first_name,
                'last_name': purchase.user.last_name,
                'email': purchase.user.email,
                'country': purchase.user.country,
            },
            'pack': {
                'id': purchase.pack.id,
                'title': purchase.pack.title,
                'description': purchase.pack.description,
            },
            'total': purchase.total,
            'buyerCard': purchase.buyerCard,
            'buyerCardName': purchase.buyerCardName,
            'buyerCardDueDate': purchase.buyerCardDueDate,
            'buyerCardCVV': purchase.buyerCardCVV,
            'createdAt': purchase.createdAt
        }
