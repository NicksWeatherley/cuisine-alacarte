from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.template import loader
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.views.generic.list import ListView

from .models import DeliveryPerson, Delivery
from .forms import BidForm

@method_decorator([login_required], name='dispatch')
class DeliveryListView(ListView):
    model = Delivery

    def get_queryset(self, **kwargs):
        user = DeliveryPerson.objects.filter(user=self.request.user.id)[0]
        return user.delivery_set.all()

def get_bid(request, purchase_id):
    if request.method == 'POST':
        form = BidForm(request.POST)
        if form.is_valid():
            _process_bid(form.cleaned_data['bid'], purchase_id)
            return HttpResponseRedirect('/deliveryperson/deliverylist')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = BidForm()

    return render(request, 'delivery_person/bid_form.html', {'form': form})

def _process_bid(bid, purchase_id):
    delivery = Delivery.objects.all()[purchase_id - 1]
    delivery.bid = bid
    delivery.status = 2
    delivery.save()