from django.db import models
from django.contrib.auth.models import User
from django.db.models import Sum, F
from django.utils.translation import gettext_lazy as _


class Food(models.Model):
    name = models.CharField(max_length=250)
    description = models.TextField()
    price = models.DecimalField(max_digits=7, decimal_places=2)

    objects = models.Manager()


class OrderManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().annotate(
            total_amount=Sum(
                F('order_items__quantity') *
                F('order_items__food__price')
            )
        )


class Order(models.Model):
    class PaymentMethod(models.TextChoices):
        CASH = 'Cash', _('Cash')
        CHECKS = 'Checks', _('Checks')
        DEBIT_CARDS = 'Debit_cards', _('Debit_cards')
        CREDIT_CARDS = 'Credit_cards', _('Credit_cards')
        MOBILE_PAYMENTS = 'MobilePayments', _('MobilePayments')

    food = models.ManyToManyField(
        Food,
        related_name='order',
        through='delivery.OrderItem'
    )
    customer = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='orders',
    )
    order_date = models.DateTimeField(auto_now_add=True)
    delivery_address = models.TextField()
    payment_method = models.CharField(
        max_length=50,
        choices=PaymentMethod.choices
    )

    objects = OrderManager()


class OrderItem(models.Model):
    order = models.ForeignKey(
        Order,
        on_delete=models.CASCADE,
        related_name='order_items'
    )
    food = models.ForeignKey(
        Food,
        on_delete=models.CASCADE,
        related_name='order_items'
    )
    quantity = models.PositiveSmallIntegerField()
