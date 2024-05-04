from django.utils import timezone
from rest_framework import viewsets
from purchase_order.models import PurchaseOrder
from purchase_order.serializers import PurchaseOrderSerializer
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated


# Create your views here.
class PurchaseOrderViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = PurchaseOrder.objects.all()
    serializer_class = PurchaseOrderSerializer

    @action(detail=True, methods=['post'])
    def acknowledge(self, request, pk=None):
        """
        Acknowledge a PurchaseOrder by updating its 'acknowledgement_date'.
        """
        purchase_order = self.get_object()
        # if the 'acknowledgement_date' is not set
        if not purchase_order.acknowledgement_date:
            try:
                # Set 'acknowledgement_date' to current timestamp
                purchase_order.acknowledgement_date = timezone.now()
                purchase_order.save()
            except Exception as e:
                print(e)
        purchase_order_detail = {
            'purchase_order': purchase_order.po_number,
            'vendor': purchase_order.vendor.name,
            'order_date': purchase_order.order_date,
            'delivery_date': purchase_order.delivery_date,
            'items': purchase_order.items,
            'quantity': purchase_order.quantity,
            'status': purchase_order.status,
            'quality_rating': purchase_order.quality_rating,
            'issue_date': purchase_order.issue_date,
            'acknowledgement_date': purchase_order.acknowledgement_date
        }
        return Response(purchase_order_detail)
