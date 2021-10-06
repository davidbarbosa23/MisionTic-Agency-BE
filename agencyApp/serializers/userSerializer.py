from rest_framework import serializers
from agencyApp.models.user import User


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ['id', 'username', 'password', 'firstName',
                  'lastName', 'email', 'country', 'birthDay', 'createdAt']

    def create(self, validated_data):
        userInstance = User.objects.create(**validated_data)
        return userInstance

    def to_representation(self, obj):
        user = User.objects.get(id=obj.id)
        return {
            'id': user.id,
            'username': user.username,
            'firstName': user.firstName,
            'lastName': user.lastName,
            'email': user.email,
            'country': user.country,
            'birthDay': user.birthDay,
            'createdAt': user.createdAt
        }
