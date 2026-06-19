from django.db import models


class Lead(models.Model):

    STATUS_CHOICES = (
        ('new', 'New'),
        ('contacted', 'Contacted'),
        ('qualified', 'Qualified'),
        ('proposal', 'Proposal'),
        ('won', 'Won'),
        ('lost', 'Lost'),
    )

    SOURCE_CHOICES = (
        ('website', 'Website'),
        ('facebook', 'Facebook'),
        ('instagram', 'Instagram'),
        ('google', 'Google'),
        ('referral', 'Referral'),
        ('other', 'Other'),
    )

    company = models.ForeignKey(
        'companies.Company',
        on_delete=models.CASCADE
    )

    assigned_to = models.ForeignKey(
        'accounts.User',
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )

    name = models.CharField(max_length=255)
    email = models.EmailField(blank=True, null=True)
    phone = models.CharField(max_length=20)

    source = models.CharField(
        max_length=50,
        choices=SOURCE_CHOICES,
        default='website'
    )

    status = models.CharField(
        max_length=50,
        choices=STATUS_CHOICES,
        default='new'
    )

    notes = models.TextField(blank=True, null=True)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name