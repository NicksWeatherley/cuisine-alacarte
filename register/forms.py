from django.contrib.auth.forms import UserCreationForm
from app_user.models import User


class UserRegistrationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = User
        fields = ["username", "email", "first_name", "last_name", "password1", "password2"]

