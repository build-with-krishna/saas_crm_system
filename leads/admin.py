from django.contrib import admin
from .models import Lead


@admin.register(Lead)
class LeadAdmin(admin.ModelAdmin):

    list_display = (
        'name',
        'phone',
        'source',
        'status',
        'company'
    )

    search_fields = (
        'name',
        'phone'
    )