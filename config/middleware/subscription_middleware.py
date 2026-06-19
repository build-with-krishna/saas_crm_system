from datetime import date

from django.shortcuts import redirect
from django.urls import reverse

from subscriptions.models import Subscription


class SubscriptionMiddleware:

    def __init__(self, get_response):

        self.get_response = get_response

    def __call__(self, request):

        if request.user.is_authenticated and not request.user.is_superuser:

            ignore_urls = [

                reverse('subscription_expired'),

                reverse('upgrade_plan'),

                '/accounts/login/',

                '/accounts/logout/',

                '/admin/'
            ]

            if request.path not in ignore_urls:

                subscription = Subscription.objects.filter(
                    company=request.user.company
                ).first()

                if subscription:

                    if subscription.end_date < date.today():

                        subscription.status = 'expired'
                        subscription.save()

                        return redirect(
                            reverse(
                                'subscription_expired'
                            )
                        )

                else:

                    return redirect(
                        reverse(
                            'subscription_expired'
                        )
                    )

        response = self.get_response(request)

        return response