from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from agencyApp.models.pack import Pack
from agencyApp.serializers.packSerializer import PackSerializer


class PackDetailView(generics.ListAPIView):
    queryset = Pack.objects.all()
    serializer_class = PackSerializer

    def get(self, request, *args, **kwargs):

        if 'id' in kwargs:
            pack = Pack.objects.get(id=kwargs['id'])
            serializer = PackSerializer(pack)
            return Response(serializer.data, status=status.HTTP_200_OK)

        return super().get(request, *args, **kwargs)
