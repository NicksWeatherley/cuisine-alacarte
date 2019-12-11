from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.template import loader
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.views.generic.list import ListView, View

from .models import Manager
from customer.models import Customer
from app_user.models import User
from restaurant.models import Restaurant

@method_decorator([login_required], name='dispatch')
class CustomerListView(ListView):
    model = Customer
    template_name = 'manager/customer_list.html'

    def get_queryset(self, **kwargs):
        restaurant = Manager.objects.filter(user=self.request.user.id)[0].restaurant_set.all()[0]
        return restaurant.customer_set.all()


@method_decorator([login_required], name='dispatch')
class EmployeeList(View):

    def get(self, request, *args, **kwargs):
        restaurant = Restaurant.objects.filter(manager=self.request.user.manager.id)[0]
        return render(request, 'manager/employee_list.html', {'restaurant': restaurant})