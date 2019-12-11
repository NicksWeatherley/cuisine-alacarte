from django.shortcuts import render

# Create your views here.
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.views.generic.list import ListView
from django.http import HttpResponseRedirect

from item.models import Dish
from .models import Cook
from .forms import NewDishForm, RemoveDishForm
from item.models import Item

# def view_cook_menu(request):
#     return render(request, "cook/dish_list.html")


@method_decorator([login_required], name='dispatch')
class DishListView(ListView):
    model = Dish

    def get_queryset(self, **kwargs):
        user = Cook.objects.filter(user=self.request.user.id)[0]
        return user.dish_set.all()


def get_new_dish(request, cook_id):
    if request.method == 'POST':
        form = NewDishForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            price = form.cleaned_data['price']
            items = form.cleaned_data['items']
            _add_new_dish(name, price, items, cook_id)
            return HttpResponseRedirect('/cook/dishlist')
    else:
        form = NewDishForm()

    return render(request, 'cook/add_dish.html', {'form': form})


def _add_new_dish(name, price, items, cook_id):
    cook = Cook.objects.all()[cook_id - 1]
    restaurant = cook.restaurant
    new_dish = Dish.objects.create(name=name, price=price, cook=cook)

    for form_item in items:
        item = Item.objects.all()[int(form_item.id) - 1]
        new_dish.items.add(item)

    new_dish.save()

    restaurant.dish_set.add(new_dish)
    restaurant.save()


def get_dishes_to_remove(request, cook_id):
    form = RemoveDishForm(request.user, request.POST)
    if form.is_valid():
        dishes = form.cleaned_data['dishes']
        _remove_dishes(dishes)
        return HttpResponseRedirect('/cook/dishlist')
    else:
        form = RemoveDishForm(request.user)

    return render(request, 'cook/remove_dish.html', {'form': form})


def _remove_dishes(dishes):
    dishes.delete()
