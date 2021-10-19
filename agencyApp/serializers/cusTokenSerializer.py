from rest_framework_simplejwt.serializers import TokenObtainPairSerializer


class CusTokenSerializer(TokenObtainPairSerializer):
    def validate(self, attrs):
        data = super(CusTokenSerializer, self).validate(attrs)
        data.update({'id': self.user.id})
        return data
