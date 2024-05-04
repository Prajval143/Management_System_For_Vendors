from rest_framework import viewsets
from vendor_performance.models import HistoricalPerformance
from vendor_performance.serializers import HistoricalPerformanceSerializer
from rest_framework.permissions import IsAuthenticated


class HistoricalPerformanceViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = HistoricalPerformance.objects.all()
    serializer_class = HistoricalPerformanceSerializer
