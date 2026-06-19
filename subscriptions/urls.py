from django.urls import path
from . import views

urlpatterns = [

    path(
        'expired/',
        views.subscription_expired,
        name='subscription_expired'
    ),

    path(
        'upgrade/',
        views.upgrade_plan,
        name='upgrade_plan'
    ),

]