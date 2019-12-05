from django.shortcuts import render
from .forms import UserRegistrationForm
from app_user.models import User
from customer.models import Customer
from cook.models import Cook
from manager.models import Manager
from salesperson.models import Salesperson
from delivery_person.models import DeliveryPerson


# Create your views here.
def register(request):
    return render(request, "register/register.html")


# Terrible repetitive code below - please don't judge me
# I need to figure out how to pass user type from register.html
def customer_register(request):
    if request.method == "POST":
        user_form = UserRegistrationForm(request.POST)
        if user_form.is_valid():
            user = user_form.save(commit=False)
            user.is_customer = True
            user.save()
            # below is repetition of the data - both user and customer that references that
            # user have first/last name and email fields
            # we can solve it by deleting these fields from Customer and accessing them from User table
            first_name = user_form.cleaned_data["first_name"]
            last_name = user_form.cleaned_data["last_name"]
            email = user_form.cleaned_data["email"]
            new_customer = Customer.objects.create(user=user, first_name=first_name, last_name=last_name, customer_email=email, customer_type='REGISTERED')
            new_customer.save()
    else:
        user_form = UserRegistrationForm()
    return render(request, "register/customer_register.html", {"user_form": user_form})


def manager_register(request):
    if request.method == "POST":
        user_form = UserRegistrationForm(request.POST)
        if user_form.is_valid():
            user = user_form.save(commit=False)
            user.is_manager = True
            user.save()
            first_name = user_form.cleaned_data["first_name"]
            last_name = user_form.cleaned_data["last_name"]
            new_manager = Manager.objects.create(user=user, first_name=first_name, last_name=last_name, salary=0)
            new_manager.save()
    else:
        user_form = UserRegistrationForm()
    return render(request, "register/manager_register.html", {"user_form": user_form})


def cook_register(request):
    if request.method == "POST":
        user_form = UserRegistrationForm(request.POST)
        if user_form.is_valid():
            user = user_form.save(commit=False)
            user.is_cook = True
            user.save()
            first_name = user_form.cleaned_data["first_name"]
            last_name = user_form.cleaned_data["last_name"]
            new_cook = Cook.objects.create(user=user, first_name=first_name, last_name=last_name, salary=0)
            new_cook.save()
    else:
        user_form = UserRegistrationForm()
    return render(request, "register/cook_register.html", {"user_form": user_form})


def delivery_person_register(request):
    if request.method == "POST":
        user_form = UserRegistrationForm(request.POST)
        if user_form.is_valid():
            user = user_form.save(commit=False)
            user.is_delivery_person = True
            user.save()
            first_name = user_form.cleaned_data["first_name"]
            last_name = user_form.cleaned_data["last_name"]
            new_delivery_person = DeliveryPerson.objects.create(user=user, first_name=first_name, last_name=last_name, salary=0)
            new_delivery_person.save()
    else:
        user_form = UserRegistrationForm()
    return render(request, "register/delivery_person_register.html", {"user_form": user_form})


def sales_person_register(request):
    if request.method == "POST":
        user_form = UserRegistrationForm(request.POST)
        if user_form.is_valid():
            user = user_form.save(commit=False)
            user.is_sales_person = True
            user.save()
            first_name = user_form.cleaned_data["first_name"]
            last_name = user_form.cleaned_data["last_name"]
            new_sales_person = Salesperson.objects.create(user=user, first_name=first_name, last_name=last_name, salary=0)
            new_sales_person.save()
    else:
        user_form = UserRegistrationForm()
    return render(request, "register/sales_person_register.html", {"user_form": user_form})
