from django.db import models


class Deal(models.Model):

    STAGE_CHOICES = (
        ('new', 'New'),
        ('qualified', 'Qualified'),
        ('proposal', 'Proposal Sent'),
        ('negotiation', 'Negotiation'),
        ('won', 'Won'),
        ('lost', 'Lost'),
    )

    company = models.ForeignKey(
        'companies.Company',
        on_delete=models.CASCADE
    )

    customer = models.ForeignKey(
        'customers.Customer',
        on_delete=models.CASCADE
    )

    assigned_to = models.ForeignKey(
        'accounts.User',
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )

    title = models.CharField(max_length=255)

    amount = models.DecimalField(
        max_digits=12,
        decimal_places=2,
        default=0
    )

    stage = models.CharField(
        max_length=50,
        choices=STAGE_CHOICES,
        default='new'
    )

    expected_close_date = models.DateField(
        null=True,
        blank=True
    )

    notes = models.TextField(
        blank=True,
        null=True
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):
        return self.title