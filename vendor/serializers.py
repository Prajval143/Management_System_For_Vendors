from rest_framework import routers, serializers, viewsets
from vendor.models import Vendor


class VendorSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Vendor
        fields = '__all__'
