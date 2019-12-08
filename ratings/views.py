from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.template import loader
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.views.generic.list import ListView
from django.contrib.auth import get_user_model

from .models import ItemRating, CustomerRating, DeliveryRating, DishRating
from customer.models import Customer
from delivery_person.models import Delivery
from cook.models import Cook
from item.models import Item, Dish

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
