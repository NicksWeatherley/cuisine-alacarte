from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.template import loader
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.views.generic.list import ListView

from .models import Manager
from customer.models import Customer

@method_decorator([login_required], name='dispatch')
class CustomerListView(ListView):
    model = Customer
    template_name = 'manager/customer_list.html'

    def get_queryset(self, **kwargs):
        restaurant = Manager.objects.filter(user=self.request.user.id)[0].restaurant_set.all()[0]
        return restaurant.customer_set.all()