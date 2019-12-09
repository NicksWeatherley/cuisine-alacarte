from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.views.generic.list import ListView
from django.contrib.auth import get_user_model

from .models import ItemRating, CustomerRating, DeliveryRating, DishRating
from .forms import RateForm

from customer.models import Customer, Order
from delivery_person.models import Delivery
from cook.models import Cook
from item.models import Item, Dish


def RateCustomer(request, customer_id):
    if request.method == 'POST':
        form = RateForm(request.POST)
        if form.is_valid():
            _process_customer_rating(
                form.cleaned_data['rating'], form.cleaned_data['notes'], customer_id)
            return HttpResponseRedirect('/deliveryperson/deliverylist')

    else:
        form = RateForm()

    return render(request, 'ratings/rate_form.html', {'form': form})

def _process_customer_rating(rating, notes, customer_id):
    customer = Customer.objects.get(id=customer_id)
    rating = CustomerRating(score = rating, note = notes, customer = customer)
    rating.save()

def RateDelivery(request, delivery_id):
    if request.method == 'POST':
        form = RateForm(request.POST)
        if form.is_valid():
            _process_delivery_rating(
                form.cleaned_data['rating'], form.cleaned_data['notes'], delivery_id)
            return HttpResponseRedirect('/customer/history')

    else:
        form = RateForm()

    return render(request, 'ratings/rate_form.html', {'form': form})

def _process_delivery_rating(rating, notes, delivery_id):
    order = Order.objects.get(id = delivery_id)
    rating = DeliveryRating(score = rating, note = notes, delivery = order.delivery)
    rating.save()

def RateDish(request, dish_id):
    if request.method == 'POST':
        form = RateForm(request.POST)
        if form.is_valid():
            _process_dish_rating(
                form.cleaned_data['rating'], form.cleaned_data['notes'], dish_id)
            return HttpResponseRedirect('/customer/history')

    else:
        form = RateForm()

    return render(request, 'ratings/rate_form.html', {'form': form})

def _process_dish_rating(rating, notes, dish_id):
    order = Order.objects.get(id = dish_id)
    for dish in order.dishes.all():
        rating = DishRating(score = rating, note = notes, item = dish)
        rating.save()
    order.status = 6
    order.save()



class ItemRatingListView(ListView):
    model = ItemRating
    template_name = 'ratings/ratings_list.html'

    def get_queryset(self, **kwargs):
        ritem = Item.objects.get(id=self.kwargs['item_id'])
        return ritem.itemrating_set.all()


class CustomerRatingListView(ListView):
    model = CustomerRating
    template_name = 'ratings/rating_list.html'

    def get_queryset(self, **kwargs):
        cust = Customer.objects.get(id=self.kwargs['item_id'])
        return cust.customerrating_set.all()


class DeliveryRatingListView(ListView):
    model = DeliveryRating
    template_name = 'ratings/rating_list.html'

    def get_queryset(self, **kwargs):
        cust = Delivery.objects.get(id=self.kwargs['item_id'])
        return cust.deliveryrating_set.all()


class DishRatingListView(ListView):
    model = DishRating
    template_name = 'ratings/rating_list.html'

    def get_queryset(self, **kwargs):
        cust = Dish.objects.get(id=self.kwargs['item_id'])
        return cust.dishrating_set.all()
