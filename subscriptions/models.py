from django.db import models


class Plan(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    duration_days = models.IntegerField(default=30)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.name


class Subscription(models.Model):

    STATUS_CHOICES = (
        ('active', 'Active'),
        ('expired', 'Expired')
    )

    company = models.ForeignKey(
        'companies.Company',
        on_delete=models.CASCADE
    )

    plan = models.ForeignKey(
        Plan,
        on_delete=models.CASCADE
    )

    start_date = models.DateField()

    end_date = models.DateField()

    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default='active'
    )

    def __str__(self):
        return self.company.name