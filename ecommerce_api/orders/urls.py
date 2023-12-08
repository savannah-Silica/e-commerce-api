from django.urls import path
from . import views

urlpatterns = [
    path('statuses/', views.order_status_list, name='order_status_list'),
    path('status/create/', views.order_status_create, name='order_status_create'),
    path('status/update/<int:pk>/', views.order_status_update, name='order_status_update'),
    path('status/delete/<int:pk>/', views.order_status_delete, name='order_status_delete'),
    path('', views.order_list, name='order_list'),
    path('create/', views.order_create, name='order_create'),
    path('update/<int:pk>/', views.order_update, name='order_update'),
    path('delete/<int:pk>/', views.order_delete, name='order_delete'),
]