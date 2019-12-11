from django.shortcuts import render
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.views.generic.list import ListView
from django.http import HttpResponseRedirect
from .models import Restaurant

# Create your views here.


class RestaurantListView(ListView):
    model = Restaurant

    # Everyone can see the list of restaurant on the main page
    def get_queryset(self, **kwargs):
        return Restaurant.objects.all()
