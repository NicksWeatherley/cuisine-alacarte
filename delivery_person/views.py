from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.template import loader
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.views.generic.list import ListView

from .models import DeliveryPerson, Delivery

@method_decorator([login_required], name='dispatch')
class PurchaseListView(ListView):
    model = Delivery

    def get_queryset(self, **kwargs):
        user = DeliveryPerson.objects.filter(user=self.request.user.id)[0]
        return user.purchase_set.all()