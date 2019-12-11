from django import forms
from django.core.validators import MaxValueValidator, MinValueValidator


class CommissionEditForm(forms.Form):
    commission = forms.FloatField(
        validators=[MinValueValidator(0.01), MaxValueValidator(0.70),],
    )