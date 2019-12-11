from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.template import loader
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.views.generic.list import ListView
from django.utils import timezone

from .models import Customer, Order
from restaurant.models import Restaurant
from .forms import CreateOrder
from item.models import Dish


@method_decorator([login_required], name='dispatch')
class CustomerListView(ListView):
    model = Customer
    template_name = 'customer/history_list.html'

    def get_queryset(self, **kwargs):
        user = Customer.objects.get(user=self.request.user.id)
        return user.order_set.all()


def get_dishes_to_order(request):
    form = CreateOrder(request.POST)
    if form.is_valid():
        dishes = form.cleaned_data['dishes']

        # _add_dishes_to_order(dishes)
        return HttpResponseRedirect('/customer/createorder')
    else:
        form = CreateOrder()

    return render(request, 'customer/create_order.html', {'form': form})


def _add_dishes_to_order(dishes):
    new_order = Order.objects.create(status="new", created=timezone.now, last_updated=timezone.now)
    new_order.save()

    for form_dish in dishes:
        # dish = Dish.objects.all()[form_dish.id - 1]
        new_order.dishes.add(form_dish)


def view_shopping_cart(request):
    return render(request, 'customer/shopping_cart.html')

