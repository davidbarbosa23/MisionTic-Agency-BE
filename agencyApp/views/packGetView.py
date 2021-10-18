from rest_framework import generics, status
from rest_framework.response import Response
from agencyApp.models.pack import Pack
from agencyApp.serializers.packSerializer import PackSerializer


class PackGetView(generics.ListAPIView):
    queryset = Pack.objects.order_by('id').filter(is_active=True)
    serializer_class = PackSerializer

    def get(self, request, *args, **kwargs):

        if 'id' in kwargs:
            pack = Pack.objects.get(id=kwargs['id'])
            serializer = PackSerializer(pack)
            return Response(serializer.data, status=status.HTTP_200_OK)

        limit = request.GET.get('limit', None)
        if (limit):
            packs = Pack.objects.order_by('id')[:int(limit)]
            serializer = PackSerializer(packs, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)

        return super().get(request, *args, **kwargs)
