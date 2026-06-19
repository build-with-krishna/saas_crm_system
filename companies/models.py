from django.db import models


class Company(models.Model):

    name = models.CharField(max_length=255)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    address = models.TextField(blank=True, null=True)

    is_active = models.BooleanField(default=True)

    created_at = models.DateTimeField(auto_now_add=True)

    is_subscription_active = models.BooleanField(
        default=True
    )

    def __str__(self):
        return self.name