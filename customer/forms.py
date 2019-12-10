from django import forms
from .models import Customer

class EditCustomerTypeForm(forms.Form):
    choice = forms.ChoiceField(choices = Customer.CUSTOMER_TYPES)