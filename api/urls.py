from rest_framework import routers
from django.urls import path, include
from vendor.views import VendorViewSet
from purchase_order.views import PurchaseOrderViewSet
from rest_framework.authtoken.views import obtain_auth_token

router = routers.DefaultRouter()

router.register('purchase_orders', PurchaseOrderViewSet)
router.register('vendors', VendorViewSet)


# URLS for API app
urlpatterns = [
    path('', include(router.urls)),
    path('auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('api-token-auth/', obtain_auth_token, name='api_token_auth'),
]
