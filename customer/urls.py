from django.urls import path

import customer.views as view

urlpatterns = [
    path('customer/history', view.CustomerListView.as_view(), name='view_history'),
    path('edit/customer/<int:customer_id>', view.EditCustomerType, name = 'edit_customer_type'),

]