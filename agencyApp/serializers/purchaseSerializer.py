from rest_framework import serializers
from agencyApp.models.purchase import Purchase
from agencyApp.models.user import User
from agencyApp.models.pack import Pack
from agencyApp.serializers.userSerializer import UserSerializer
from agencyApp.serializers.packSerializer import PackSerializer


class PurchaseSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    pack = PackSerializer()

    class Meta:
        model = Purchase
        fields = ['id', 'user', 'pack', 'total', 'buyerCard',
                  'buyerCardName', 'buyerCardDueDate', 'buyerCardCVV', 'createdAt']

    def create(self, validated_data):
        purchaseInstance = Purchase.objects.create(**validated_data)
        return purchaseInstance

    def to_representation(self, obj):
        user = User.objects.get(id=obj.user)
        pack = Pack.objects.get(id=obj.pack)
        purchase = Purchase.objects.get(id=obj.id)
        return {
            'id': purchase.id,
            'user': {
                'id': user.id,
                'firstName': user.firstName,
                'lastName': user.lastName,
                'email': user.email,
                'counrty': user.counrty,
            },
            'pack': {
                'id': pack.id,
                'title': pack.title,
                'description': pack.description,
            },
            'total': purchase.total,
            'buyerCard': purchase.buyerCard,
            'buyerCardName': purchase.buyerCardName,
            'buyerCardDueDate': purchase.buyerCardDueDate,
            'buyerCardCVV': purchase.buyerCardCVV,
            'createdAt': purchase.createdAt
        }
