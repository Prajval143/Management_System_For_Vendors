from django.db import models
from django.db.models import Avg
from django.db.models import F
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.utils import timezone
from vendor.models import Vendor


class PurchaseOrder(models.Model):
    # PO Model
    po_number = models.CharField(max_length=100, unique=True, blank=True)
    vendor = models.ForeignKey(Vendor, on_delete=models.CASCADE, null=True, db_constraint=False)
    order_date = models.DateTimeField(auto_now_add=True)
    delivery_date = models.DateTimeField()
    items = models.JSONField()
    quantity = models.IntegerField()
    status = models.CharField(max_length=50, default="Pending")
    quality_rating = models.FloatField(null=True, blank=True)
    issue_date = models.DateTimeField(null=True, blank=True)
    acknowledgement_date = models.DateTimeField(null=True, blank=True)
    completion_date = models.DateTimeField(null=True, blank=True)


@receiver(post_save, sender=PurchaseOrder)
def update_vendor_performance(sender, instance, **kwargs):
    """
    after saving the po updates the vendor performance
    """
    if instance.status == 'completed' and instance.delivery_date is None:
        instance.delivery_date = timezone.now()
        instance.save()

    # Update On-Time Delivery Rate
    completed_orders = PurchaseOrder.objects.filter(vendor=instance.vendor, status='completed')
    # on_time_delivery_rate = completed_orders.filter(delivery_date__lte=instance.delivery_date).count() /
    # completed_orders.count()
    on_time_deliveries = completed_orders.filter(delivery_date__gte=F('delivery_date'))
    if completed_orders.count() != 0:
        on_time_delivery_rate = on_time_deliveries.count() / completed_orders.count()
    else:
        on_time_delivery_rate = 0
    instance.vendor.on_time_delivery_rate = on_time_delivery_rate if on_time_delivery_rate else 0

    # Update Quality Rating Average
    completed_orders_with_rating = completed_orders.exclude(quality_rating__isnull=True)
    quality_rating_avg = completed_orders_with_rating.aggregate(Avg('quality_rating'))['quality_rating__avg'] or 0
    instance.vendor.quality_rating_avg = quality_rating_avg if quality_rating_avg else 0
    instance.vendor.save()


@receiver(post_save, sender=PurchaseOrder)
def update_response_time(sender, instance, **kwargs):
    """
        after saving the po updates the response time of vendor
    """
    response_times = PurchaseOrder.objects.filter(vendor=instance.vendor,
                                                  acknowledgement_date__isnull=False).values_list(
        'acknowledgement_date',
        'issue_date')
    average_response_time = sum(
        (ack_date - issue_date).total_seconds() for ack_date, issue_date in response_times)  # / len(response_times)
    if average_response_time < 0:
        average_response_time = 0
    if response_times:
        average_response_time = average_response_time / len(response_times)
    else:
        average_response_time = 0  # Avoid division by zero if there are no response times
    instance.vendor.average_response_time = average_response_time
    instance.vendor.save()


@receiver(post_save, sender=PurchaseOrder)
def update_fulfillment_rate(sender, instance, **kwargs):
    """
        after saving po updates the fulfillment_rate
    """
    fulfilled_orders = PurchaseOrder.objects.filter(vendor=instance.vendor,
                                                    status='completed')  # , quality_rating__isnull=False)
    fulfillment_rate = fulfilled_orders.count() / PurchaseOrder.objects.filter(vendor=instance.vendor).count()
    instance.vendor.fulfillment_rate = fulfillment_rate
    instance.vendor.save()
