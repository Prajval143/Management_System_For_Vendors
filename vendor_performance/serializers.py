from rest_framework import routers, serializers, viewsets
from vendor_performance.models import HistoricalPerformance


class HistoricalPerformanceSerializer(serializers.ModelSerializer):
    class Meta:
        model = HistoricalPerformance
        fields = '__all__'
