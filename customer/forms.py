from django import forms
from item.models import Item, Dish
from restaurant.models import Restaurant
from .models import Customer


class CreateOrder(forms.Form):
    dishes = forms.ModelMultipleChoiceField(queryset=Dish.objects.all(), widget=forms.CheckboxSelectMultiple,
                                           required=True, label='Dishes you want to add to your order:')

    fields = ["dishes"]
    #
    # def __init__(self, restaurant, user, *args, **kwargs):
    #     super(CreateOrder, self).__init__(*args, **kwargs)
    #     self.fields['dishes'].queryset = Dish.objects.filter(restaurant=restaurant)
