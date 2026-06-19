"""
URL configuration for config project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include, re_path

from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

from django.urls import re_path


schema_view = get_schema_view(
    openapi.Info(
        title="CRM API",
        default_version='v1',
        description="SaaS CRM API Documentation",
    ),
    public=True,
    permission_classes=[permissions.AllowAny],
)

urlpatterns = [

    path('admin/', admin.site.urls),

    path('accounts/', include('accounts.urls')),

    path('dashboard/', include('dashboard.urls')),

    path('leads/', include('leads.urls')),

    path('customers/', include('customers.urls')),
    
    path('deals/', include('deals.urls')),

    path('tasks/', include('tasks_app.urls')),

    path('followups/', include('followups.urls')),

    path(
        'subscription/',
        include('subscriptions.urls')
    ),
    
    path(
        'superadmin/',
        include('superadmin_panel.urls')
    ),

    path(
        'api/',
        include('api.urls')
    ),

    re_path(
        r'^swagger/$',
        schema_view.with_ui(
            'swagger',
            cache_timeout=0
        ),
        name='schema-swagger-ui'
    ),

]




