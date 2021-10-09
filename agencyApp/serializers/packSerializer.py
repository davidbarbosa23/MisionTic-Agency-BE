from rest_framework import serializers
from agencyApp.models.pack import Pack


class PackSerializer(serializers.ModelSerializer):

    class Meta:
        model = Pack
        fields = ['id', 'title', 'description', 'price', 'is_active',
                  'discount', 'country', 'image_url', 'created_at', 'modified_at']

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
            'is_active': pack.is_active,
            'discount': pack.discount,
            'country': pack.country,
            'image_url': pack.image_url,
            'created_at': pack.created_at,
            'modified_at': pack.modified_at
        }
