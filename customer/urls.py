from django.urls import path

import customer.views as view

urlpatterns = [
    path('customer/history', view.CustomerListView.as_view(), name='view_history'),
]