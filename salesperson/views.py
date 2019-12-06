from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.template import loader
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.views.generic.list import ListView

from salesperson.models import Purchase, Salesperson

# TODO: Get current logged in user data to get salesperson data
@method_decorator([login_required], name='dispatch')
class PurchaseListView(ListView):
    model = Purchase

    def get_queryset(self, **kwargs):
        user = Salesperson.objects.filter(user=self.request.user.id)[0]
        return user.purchase_set.all()


def purchase_detail(request):
    return render(request, '')
