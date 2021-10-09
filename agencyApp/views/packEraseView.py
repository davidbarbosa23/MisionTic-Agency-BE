from django.shortcuts import get_object_or_404
from rest_framework import views
from rest_framework.response import Response
from agencyApp.models.pack import Pack


class PackEraseView(views.APIView):
    def delete(self, request, id=None):
        item = get_object_or_404(Pack, id=id)
        item.delete()
        return Response({"status": "success", "data": "Item Deleted"})
