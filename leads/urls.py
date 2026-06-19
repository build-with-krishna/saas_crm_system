from django.urls import path
from . import views

urlpatterns = [

    path('', views.lead_list, name='lead_list'),

    path('add/', views.lead_create, name='lead_create'),

    path(
        'edit/<int:pk>/',
        views.lead_update,
        name='lead_update'
    ),

    path(
        'delete/<int:pk>/',
        views.lead_delete,
        name='lead_delete'
    ),

]