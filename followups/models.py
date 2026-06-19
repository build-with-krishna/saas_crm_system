from django.db import models


class FollowUp(models.Model):

    company = models.ForeignKey(
        'companies.Company',
        on_delete=models.CASCADE
    )

    customer = models.ForeignKey(
        'customers.Customer',
        on_delete=models.CASCADE,
        null=True,
        blank=True
    )

    deal = models.ForeignKey(
        'deals.Deal',
        on_delete=models.CASCADE,
        null=True,
        blank=True
    )

    notes = models.TextField()

    followup_date = models.DateField()

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):
        return self.notes[:50]