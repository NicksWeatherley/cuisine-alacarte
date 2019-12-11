from django.urls import path

from .views import CustomerListView, EmployeeList

urlpatterns = [
    path('manager/customerlist', CustomerListView.as_view(), name='customer_list'),
    path('manager/employeelist', EmployeeList.as_view(), name='employee_list'),

]
