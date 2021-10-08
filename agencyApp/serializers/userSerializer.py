from rest_framework import serializers
from django.contrib.auth.hashers import make_password
from agencyApp.models.user import User


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ['id', 'username', 'password', 'first_name',
                  'last_name', 'email', 'country', 'birthDay', 'createdAt']

    def create(self, validated_data):
        userInstance = User.objects.create(**validated_data)
        return userInstance

    def validate_password(self, value: str) -> str:
        return make_password(value)

    def to_representation(self, obj):
        user = User.objects.get(id=obj.id)
        return {
            'id': user.id,
            'username': user.username,
            'first_name': user.first_name,
            'last_name': user.last_name,
            'email': user.email,
            'country': user.country,
            'birthDay': user.birthDay,
            'createdAt': user.createdAt
        }
