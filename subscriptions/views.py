from django.shortcuts import render
from .models import Plan


def subscription_expired(request):

    return render(
        request,
        'subscriptions/expired.html'
    )


def upgrade_plan(request):

    plans = Plan.objects.filter(
        is_active=True
    )

    return render(
        request,
        'subscriptions/upgrade.html',
        {
            'plans': plans
        }
    )