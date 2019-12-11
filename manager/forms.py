from django import forms
from django.core.validators import MaxValueValidator, MinValueValidator


class ChangePayForm(forms.Form):
    pay = forms.FloatField(
        validators=[MinValueValidator(0.01),],
    )