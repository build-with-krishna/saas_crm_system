from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from datetime import date
from subscriptions.models import Subscription


@login_required
def dashboard(request):

    subscription = Subscription.objects.filter(
        company=request.user.company,
        status='active'
    ).first()

    remaining_days = 0

    if subscription:
        remaining_days = (
            subscription.end_date - date.today()
        ).days

    context = {
        'user_name': request.user.name,
        'email': request.user.email,
        'role': request.user.role,
        'company': request.user.company,
        'subscription': subscription,
        'remaining_days': remaining_days
    }

    return render(
        request,
        'dashboard/index.html',
        context
    )