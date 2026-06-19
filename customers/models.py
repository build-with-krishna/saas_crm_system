from django.db import models


class Customer(models.Model):

    CUSTOMER_TYPES = (
        ('retail', 'Retail'),
        ('wholesale', 'Wholesale'),
    )

    company = models.ForeignKey(
        'companies.Company',
        on_delete=models.CASCADE
    )

    name = models.CharField(max_length=255)

    phone = models.CharField(
        max_length=20,
        blank=True,
        null=True
    )

    email = models.EmailField(
        blank=True,
        null=True
    )

    gst_number = models.CharField(
        max_length=50,
        blank=True,
        null=True
    )

    customer_type = models.CharField(
        max_length=20,
        choices=CUSTOMER_TYPES,
        default='retail'
    )

    address = models.TextField(
        blank=True,
        null=True
    )

    outstanding_balance = models.DecimalField(
        max_digits=12,
        decimal_places=2,
        default=0
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):
        return self.name