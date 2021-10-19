from rest_framework_simplejwt.views import TokenObtainPairView
from agencyApp.serializers.cusTokenSerializer import CusTokenSerializer


class CusTokenView(TokenObtainPairView):
    serializer_class = CusTokenSerializer
