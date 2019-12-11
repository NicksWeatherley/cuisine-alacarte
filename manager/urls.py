from django.urls import path

from .views import CustomerListView, EmployeeList, EditPayCook, EditPayDeliveryPerson

urlpatterns = [
    path('manager/customerlist', CustomerListView.as_view(), name='customer_list'),
    path('manager/employeelist', EmployeeList.as_view(), name='employee_list'),
    path('manager/cookpay/<int:cook_id>', EditPayCook, name='cook_salary_change'),
    path('manager/deliverypersonpay/<int:delivery_person_id>', EditPayDeliveryPerson, name='delivery_person_salary_change'),    
]
