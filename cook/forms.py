from django import forms
from item.models import Item, Dish


class NewDishForm(forms.Form):
    name = forms.CharField(max_length=25)
    items = forms.ModelMultipleChoiceField(queryset=Item.objects.all(), widget=forms.CheckboxSelectMultiple,
                                              required=True)
    price = forms.FloatField(required=True)

    class Meta:
        model = Dish

        fields = ["name", "items", "price"]


class RemoveDishForm(forms.Form):
    dishes = forms.ModelMultipleChoiceField(queryset=Dish.objects.all(), widget=forms.CheckboxSelectMultiple,
                                           required=True, label='Dishes you want to remove:')

    fields = ["dishes"]

    def __init__(self, user, *args, **kwargs):
        super(RemoveDishForm, self).__init__(*args, **kwargs)
        self.fields['dishes'].queryset = Dish.objects.filter(cook=user.cook)