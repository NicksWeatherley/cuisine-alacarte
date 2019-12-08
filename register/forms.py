from django.contrib.auth.forms import UserCreationForm
from app_user.models import User
from restaurant.models import Restaurant
from django import forms
from django.db.utils import OperationalError

class UserRegistrationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = User

        fields = ["username", "email", "first_name", "last_name", "password1", "password2"]


class EmployeeRegistrationForm(UserCreationForm):
    try:
        restaurant = forms.CharField(label='Restaurant', widget=forms.Select(
            choices=Restaurant.objects.all().values_list('id', 'name')), required=True)
    except OperationalError:
        restaurant = forms.CharField(max_length=20, required=False)

    class Meta(UserCreationForm.Meta):
        model = User
        fields = ["username", "email", "first_name", "last_name", "password1", "password2", "restaurant"]

