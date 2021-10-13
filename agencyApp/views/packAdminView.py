from django.shortcuts import get_object_or_404
from rest_framework import status, views
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from agencyApp.models.pack import Pack
from agencyApp.serializers.packSerializer import PackSerializer


class PackAdminView(views.APIView):
    permission_classes = (IsAuthenticated,)

    def post(self, request):
        if not request.user.is_admin:
            return Response({'detail': 'Unauthorized Request'}, status=status.HTTP_403_FORBIDDEN)

        serializer = PackSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def patch(self, request, id=None):
        if not request.user.is_admin:
            return Response({'detail': 'Unauthorized Request'}, status=status.HTTP_403_FORBIDDEN)

        pack = get_object_or_404(Pack, id=id)
        serializer = PackSerializer(pack, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id=None):
        if not request.user.is_admin:
            return Response({'detail': 'Unauthorized Request'}, status=status.HTTP_403_FORBIDDEN)

        pack = get_object_or_404(Pack, id=id)
        pack.delete()
        return Response({"status": "success", "data": "Pack Deleted"}, status=status.HTTP_200_OK)
