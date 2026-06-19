from django.urls import path
from . import views

urlpatterns = [

    path(
        '',
        views.admin_dashboard,
        name='admin_dashboard'
    ),

    path(
        'companies/',
        views.company_list,
        name='company_list'
    ),

    path(
        'company/suspend/<int:pk>/',
        views.company_suspend,
        name='company_suspend'
    ),

    path(
        'company/activate/<int:pk>/',
        views.company_activate,
        name='company_activate'
    ),

    path(
        'subscriptions/',
        views.subscription_list,
        name='subscription_list'
    ),

    path(
        'assign-plan/<int:company_id>/',
        views.assign_plan,
        name='assign_plan'
    ),

]