from django.shortcuts import render

# Create your views here.
from django.utils.decorators import method_decorator


def view_cook_menu(request):
    return render(request, "cook/cook_menu.html")





