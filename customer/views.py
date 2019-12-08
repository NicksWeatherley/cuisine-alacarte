from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.template import loader
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.views.generic.list import ListView

from .models import Customer

@method_decorator([login_required], name='dispatch')
class CustomerListView(ListView):
    model = Customer
    template_name = 'customer/history_list.html'

    def get_queryset(self, **kwargs):
        user = Customer.objects.get(user = self.request.user.id)
        return user.order_set.all()