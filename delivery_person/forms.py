from django import forms
from django.core.validators import MinValueValidator

class BidForm(forms.Form):
    bid = forms.FloatField(
        validators=[MinValueValidator(0.01)],
    )