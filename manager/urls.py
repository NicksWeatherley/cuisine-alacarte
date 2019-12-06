from django.urls import path

from .views import CustomerListView

urlpatterns = [
    path('manager/customerlist', CustomerListView.as_view(), name='customer_list'),
]
