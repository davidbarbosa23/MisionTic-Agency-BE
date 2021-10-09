from rest_framework import views
from rest_framework.response import Response
from agencyApp.models.pack import Pack
from agencyApp.serializers.packSerializer import PackSerializer


class PackEditView(views.APIView):
    def patch(self, request, id=None):
        pack = Pack.objects.get(id=id)
        serializer = PackSerializer(pack, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({"status": "success", "data": serializer.data})
        else:
            return Response({"status": "error", "data": serializer.errors})
