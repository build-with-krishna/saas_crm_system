from django.contrib import admin
from .models import Customer


@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):

    list_display = (
        'name',
        'phone',
        'customer_type',
        'outstanding_balance',
        'company'
    )

    search_fields = (
        'name',
        'phone'
    )