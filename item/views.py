from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.template import loader
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.views.generic.list import ListView

from .models import Item
from cook.models import Cook

@method_decorator([login_required], name='dispatch')
class ItemListView(ListView):
    model = Item
    template_name = 'ratings/item_list.html'

    def get_queryset(self, **kwargs):
        user = Cook.objects.filter(user=self.request.user.id)[0]
        return Item.objects.filter(restaurant = user.restaurant.id)