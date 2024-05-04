from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APIClient
from rest_framework import status
from .models import Vendor
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token


class VendorModelTestCase(TestCase):
    def setUp(self):
        # Creating a Vendor for testing
        self.vendor = Vendor.objects.create(
            name='Vendor 6',
            contact_details='Contact info 6',
            address='Address 6',
            vendor_code='VN006',
            on_time_delivery_rate=0,
            quality_rating_avg=0,
            average_response_time=0,
            fulfillment_rate=0
        )

    def test_vendor_creation(self):
        # Testing Vendor creation
        vendor = Vendor.objects.get(vendor_code='VN006')
        self.assertEqual(vendor.name, 'Vendor 6')

    def test_vendor_update_method(self):
        # Testing Vendor detail update
        vendor = Vendor.objects.get(vendor_code='VN006')
        vendor.address = "Mumbai"
        vendor.save()
        self.assertEqual(vendor.address, 'Mumbai')

    def test_vendor_delete_method(self):
        # Testing Vendor object delete
        vendor = Vendor.objects.get(vendor_code='VN006')
        vendor.delete()
        vendors = Vendor.objects.all()
        self.assertEqual(vendors.count(),0)

    def test_vendor_get_all_vendor(self):
        # Testing fetching of all vendors
        vendors = Vendor.objects.all()
        self.assertEqual(vendors.count(),1)


class VendorEndpointTestCase(TestCase):
    def setUp(self):
        # Setting up the test client and user
        self.client = APIClient()
        self.user = User.objects.create_user(username='test07', password='test07')
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

    def test_get_vendor(self):
        # Testing GET request for Vendor details
        url = reverse('vendor-detail', kwargs={'pk': self.vendor.pk})
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_create_vendor(self):
        # Testing POST request to create a new Vendor
        url = reverse('vendor-list')
        data = {
            'name': 'New Vendor',
            'contact_details': 'Contact info',
            'address': 'New Address',
            'vendor_code': 'VN008',
        }
        response = self.client.post(url, data=data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_update_vendor(self):
        # Testing PUT request to update a  Vendor Detail
        url = reverse('vendor-detail', kwargs={'pk': 1})
        data = {
            'name': 'New Vendor 2',
            'contact_details': 'Contact info',
            'address': 'New Address',
            'vendor_code': 'VN009',
        }
        response = self.client.put(url, data=data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_delete_vendor(self):
        # Testing DELETE request to delete a  Vendor Detail
        url = reverse('vendor-detail', kwargs={'pk': 1})
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_get_all_vendors(self):
        # Testing fetching the list of all vendors
        url = reverse('vendor-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_vendor_performance_by_id(self):
        # Testing GET request for getting the performance details of vendors
        url = reverse('vendor-performance',kwargs={'pk': 1})
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)


