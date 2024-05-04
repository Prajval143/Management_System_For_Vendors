from datetime import timedelta
from django.contrib.auth.models import User
from django.test import TestCase
from django.urls import reverse
from django.utils import timezone
from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.test import APIClient
from vendor.models import Vendor
from .models import PurchaseOrder


class PurchaseOrderModelTestCase(TestCase):
    def setUp(self):
        # Creating a test Vendor
        self.vendor = Vendor.objects.create(
            name='Vendor 5',
            contact_details='123456789',
            address='Mumbai',
            vendor_code='VN005',
            on_time_delivery_rate=0,
            quality_rating_avg=0,
            average_response_time=0,
            fulfillment_rate=0
        )

        # Creating a test PurchaseOrder
        self.purchase_order = PurchaseOrder.objects.create(
            po_number='PO0005',
            vendor=self.vendor,
            order_date=timezone.now(),
            delivery_date=timezone.now() + timedelta(days=7),
            items={'item1': 'Headphones', 'item2': 'PC'},
            quantity=10,
            status='Completed',
            quality_rating=None,
            issue_date=timezone.now(),
            acknowledgement_date=None
        )

    def test_purchase_orders_creation(self):
        # Testing PO creation
        po = PurchaseOrder.objects.get(po_number='PO0005')
        self.assertEqual(po.vendor.name, 'Vendor 5')

    def test_get_purchase_orders_by_id(self):
        # Testing PO fetching by id
        po = PurchaseOrder.objects.get(id="1")
        self.assertEqual(po.vendor.name, 'Vendor 5')

    def test_update_purchase_orders_by_id(self):
        # Testing PO update
        po = PurchaseOrder.objects.get(id="1")
        po.vendor.name = "vendor 7"
        po.save()
        po = PurchaseOrder.objects.get(id="1")
        self.assertEqual(po.vendor.name, 'vendor 7')

    def test_delete_purchase_orders_by_id(self):
        # Testing PO delete
        po = PurchaseOrder.objects.get(id="1")
        po.delete()
        pos = PurchaseOrder.objects.all()
        self.assertEqual(pos.count(), 0)

    def test_get_all_purchase_orders(self):
        # Testing retrieving of all PO
        pos = PurchaseOrder.objects.all()
        self.assertEqual(pos.count(), 1)


class PurchaseOrderEndpointTestCase(TestCase):
    def setUp(self):
        # Setting up the test client and user
        self.client = APIClient()
        self.user = User.objects.create_user(username='test_01', password='test_01')
        self.token = Token.objects.create(user=self.user)
        self.client.credentials(HTTP_AUTHORIZATION=f'Token {self.token}')
        # Creating a Vendor for endpoint testing
        self.vendor = Vendor.objects.create(
            name='Vendor 7',
            contact_details='Contact info 7',
            address='Address 7',
            vendor_code='VN007',
            on_time_delivery_rate=0,
            quality_rating_avg=0,
            average_response_time=0,
            fulfillment_rate=0
        )
        # Creating a PO for endpoint testing
        self.purchase_order = PurchaseOrder.objects.create(
            po_number='PO0005',
            vendor=self.vendor,
            order_date=timezone.now(),
            delivery_date=timezone.now() + timedelta(days=7),
            items={'item1': 'Headphones', 'item2': 'PC'},
            quantity=10,
            status='Completed',
            quality_rating=None,
            issue_date=timezone.now(),
            acknowledgement_date=None
        )

    def test_po_generation(self):
        # Testing PO creation
        url = reverse('purchaseorder-list')
        data = {
            "po_number": "12345678901122312",
            "items": {
                "item": "Iphone Pro"
            },
            "delivery_date": "2024-05-01T10:08:11Z",
            "issue_date": "2024-04-01T10:08:11Z",
            "quantity": 1,
            "status": "completed",
            "vendor": 1
        }
        response = self.client.post(url, data=data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_get_purchase_order_by_id(self):
        # Test for PurchaseOrder retrieving
        url = reverse('purchaseorder-detail', kwargs={'pk': self.vendor.pk})
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_update_purchase_order_by_id(self):
        # Test for PurchaseOrder Updating Process
        url = reverse('purchaseorder-detail', kwargs={'pk': self.vendor.pk})
        data = {
            "po_number": "12345678901122312",
            "items": {
                "item": "Iphone Pro"
            },
            "delivery_date": "2024-05-01T10:08:11Z",
            "issue_date": "2024-04-01T10:08:11Z",
            "quantity": 1,
            "status": "completed",
            "vendor": 1
        }
        response = self.client.put(url, data=data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_delete_purchase_order_by_id(self):
        # Test for PurchaseOrder deleting process
        url = reverse('purchaseorder-detail', kwargs={'pk': self.vendor.pk})
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_get_all_po(self):
        # Test for retrieving all PO
        url = reverse('purchaseorder-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_ack_po(self):
        # Test for PurchaseOrder ACK
        url = reverse('purchaseorder-acknowledge', kwargs={'pk': self.vendor.pk})
        response = self.client.post(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
