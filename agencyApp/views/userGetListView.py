from rest_framework import generics
from agencyApp.models.user import User
from agencyApp.serializers.userSerializer import UserSerializer


class UserGetListView(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
 
    

