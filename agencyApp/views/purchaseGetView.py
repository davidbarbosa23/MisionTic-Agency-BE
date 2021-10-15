from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from agencyApp.models.purchase import Purchase
from agencyApp.serializers.purchaseSerializer import PurchaseSerializer


class PurchaseGetView(generics.ListAPIView):
    queryset = Purchase.objects.all()
    serializer_class = PurchaseSerializer
    permission_classes = (IsAuthenticated,)

    def get(self, request, *args, **kwargs):

        if 'id' in kwargs:
            purchase = Purchase.objects.get(id=kwargs['id'])

            if ((not request.user.is_admin and purchase.user.id != request.user.id)):
                return Response({'detail': 'Unauthorized Request'}, status=status.HTTP_403_FORBIDDEN)

            serializer = PurchaseSerializer(purchase)
            return Response(serializer.data, status=status.HTTP_200_OK)

        if not request.user.is_admin:
            return Response({'detail': 'Unauthorized Request'}, status=status.HTTP_403_FORBIDDEN)

        return super().get(request, *args, **kwargs)
