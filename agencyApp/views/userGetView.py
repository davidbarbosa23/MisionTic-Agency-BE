from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from agencyApp.models.user import User
from agencyApp.serializers.userSerializer import UserSerializer


class UserGetView(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (IsAuthenticated,)

    def get(self, request, *args, **kwargs):

        if ('id' in kwargs and (not request.user.is_admin and request.user.id != kwargs['id'])) or ('id' not in kwargs and not request.user.is_admin):
            return Response({'detail': 'Unauthorized Request'}, status=status.HTTP_401_UNAUTHORIZED)

        if 'id' in kwargs:
            user = User.objects.get(id=kwargs['id'])
            serializer = UserSerializer(user)
            return Response(serializer.data, status=status.HTTP_200_OK)

        return super().get(request, *args, **kwargs)
