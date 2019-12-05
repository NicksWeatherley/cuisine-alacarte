from django.urls import path

from . import views

urlpatterns = [
    path('register/', views.register, name='register'),
    path('customer_register/', views.customer_register, name='customer_register'),
    path('cook_register', views.cook_register, name='cook_register'),
    path('delivery_person_register/', views.delivery_person_register, name='delivery_person_register'),
    path('manager_register', views.manager_register, name='manager_register'),
    path('sales_person_register/', views.sales_person_register, name='sales_person_register'),
]

