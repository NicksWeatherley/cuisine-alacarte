from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.template import loader
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.views.generic.list import ListView

from .models import Customer
from .forms import EditCustomerTypeForm

@method_decorator([login_required], name='dispatch')
class CustomerListView(ListView):
    model = Customer
    template_name = 'customer/history_list.html'

    def get_queryset(self, **kwargs):
        user = Customer.objects.get(user = self.request.user.id)
        return user.order_set.all()


def EditCustomerType(request, customer_id):
    if request.method == 'POST':
        form = EditCustomerTypeForm(request.POST)
        if form.is_valid():
            _process_customer_rating(
                form.cleaned_data['choice'], customer_id)
            return HttpResponseRedirect('/manager/customerlist')

    else:
        form = EditCustomerTypeForm()

    return render(request, 'ratings/rate_form.html', {'form': form})

def _process_customer_rating(choice, customer_id):
    customer = Customer.objects.get(id=customer_id)
    print(Customer.CUSTOMER_TYPES)
    print('\n\n\n\n' + choice)
    customer.customer_type = choice
    customer.save()