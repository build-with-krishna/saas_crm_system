from django.urls import path, include
from .views import *
from rest_framework.routers import DefaultRouter

from .views import (
    LeadViewSet,
    CustomerViewSet,
    DealViewSet
)

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView
)

router = DefaultRouter()

router.register(
    'leads',
    LeadViewSet,
    basename='lead'
)

router.register(
    'customers',
    CustomerViewSet,
    basename='customer'
)

router.register(
    'deals',
    DealViewSet,
    basename='deal'
)


router.register(
    'tasks',
    TaskViewSet,
    basename='task'
)

router.register(
    'followups',
    FollowUpViewSet,
    basename='followup'
)

router.register(
    'company',
    CompanyViewSet,
    basename='company'
)

router.register(
    'profile',
    ProfileViewSet,
    basename='profile'
)

urlpatterns = [

    path(
        'token/',
        TokenObtainPairView.as_view()
    ),

    path(
        'token/refresh/',
        TokenRefreshView.as_view()
    ),

    path(
        '',
        include(router.urls)
    ),

    path(
        'dashboard/',
        DashboardAPIView.as_view()
    ),

]