from django.contrib.auth.forms import UserCreationForm
from app_user.models import User
from restaurant.models import Restaurant
from django import forms



class UserRegistrationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = User

        fields = ["username", "email", "first_name", "last_name", "password1", "password2"]


class EmployeeRegistrationForm(UserCreationForm):
    restaurant = forms.CharField(label='Restaurant', widget=forms.Select(
        choices=Restaurant.objects.all().values_list('id','name')),required=True)

    class Meta(UserCreationForm.Meta):
        model = User
        fields = ["username", "email", "first_name", "last_name", "password1", "password2", "restaurant"]


