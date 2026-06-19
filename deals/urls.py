from django.urls import path
from . import views

urlpatterns = [

    path('', views.deal_list, name='deal_list'),

    path('add/', views.deal_create, name='deal_create'),

    path(
        'edit/<int:pk>/',
        views.deal_update,
        name='deal_update'
    ),

    path(
        'delete/<int:pk>/',
        views.deal_delete,
        name='deal_delete'
    ),

    path(
        'detail/<int:pk>/',
        views.deal_detail,
        name='deal_detail'
    ),

]