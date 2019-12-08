from django.shortcuts import render

# Create your views here.
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.views.generic.list import ListView
from item.models import Dish
from .models import Cook

# def view_cook_menu(request):
#     return render(request, "cook/dish_list.html")


@method_decorator([login_required], name='dispatch')
class DishListView(ListView):
    model = Dish

    def get_queryset(self, **kwargs):
        user = Cook.objects.filter(user=self.request.user.id)[0]
        return user.dish_set.all()

