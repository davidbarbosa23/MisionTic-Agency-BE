from rest_framework import serializers
from agencyApp.models.pack import Pack


class PackSerializer(serializers.ModelSerializer):

    class Meta:
        model = Pack
        fields = ['id', 'title', 'description', 'price', 'isActive',
                  'discount', 'country', 'createdAt', 'modifiedAt']

    def create(self, validated_data):
        packInstance = Pack.objects.create(**validated_data)
        return packInstance

    def to_representation(self, obj):
        pack = Pack.objects.get(id=obj.id)
        return {
            'id': pack.id,
            'title': pack.title,
            'description': pack.description,
            'price': pack.price,
            'isActive': pack.isActive,
            'discount': pack.discount,
            'country': pack.country,
            'createdAt': pack.createdAt,
            'modifiedAt': pack.modifiedAt
        }
