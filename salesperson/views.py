from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse,HttpResponseRedirect
from django.template import loader
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.views.generic.list import ListView

from salesperson.models import Purchase, Salesperson

from .forms import CommissionEditForm


@method_decorator([login_required], name='dispatch')
class PurchaseListView(ListView):
    model = Purchase

    def get_queryset(self, **kwargs):
        user = Salesperson.objects.filter(user=self.request.user.id)[0]
        return user.purchase_set.all()


def EditCommission(request, salesperson_id):
    if request.method == 'POST':
        form = CommissionEditForm(request.POST)
        if form.is_valid():
            _process_commission_change(
                form.cleaned_data['commission'],
                salesperson_id
            )
            return HttpResponseRedirect('/manager/employeelist')

    else:
        form = CommissionEditForm()

    return render(request, 'salesperson/edit_commission_form.html', {'form': form})


def _process_commission_change(commission,salesperson_id):
    salesperson = Salesperson.objects.get(id=salesperson_id)
    salesperson.commission = commission
    salesperson.save()
