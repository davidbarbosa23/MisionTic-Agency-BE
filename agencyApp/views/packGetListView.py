from rest_framework import generics
from agencyApp.models.pack import Pack
from agencyApp.serializers.packSerializer import PackSerializer


class PackGetListView(generics.ListCreateAPIView):
    queryset = Pack.objects.all()
    serializer_class = PackSerializer
