from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.views.generic.list import ListView, View

from .models import Manager
from .forms import ChangePayForm

from app_user.models import User
from cook.models import Cook
from customer.models import Customer
from delivery_person.models import DeliveryPerson
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

def EditPayCook(request, cook_id):
    if request.method == 'POST':
        form = ChangePayForm(request.POST)
        if form.is_valid():
            _process_pay_change_cook(
                form.cleaned_data['pay'],
                cook_id
            )
            return HttpResponseRedirect('/manager/employeelist')

    else:
        form = ChangePayForm()

    return render(request, 'manager/edit_pay_form.html', {'form': form})


def _process_pay_change_cook(salary, cook_id):
    cook = Cook.objects.get(id=cook_id)
    cook.salary = salary
    cook.save()

def EditPayDeliveryPerson(request, delivery_person_id):
    if request.method == 'POST':
        form = ChangePayForm(request.POST)
        if form.is_valid():
            _process_pay_change_del(
                form.cleaned_data['pay'],
                delivery_person_id
            )
            return HttpResponseRedirect('/manager/employeelist')

    else:
        form = ChangePayForm()

    return render(request, 'manager/edit_pay_form.html', {'form': form})


def _process_pay_change_del(salary, delivery_person_id):
    delivery_person = DeliveryPerson.objects.get(id=delivery_person_id)
    delivery_person.salary = salary
    delivery_person.save()