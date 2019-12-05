from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.template import loader


# Create your views here.

def home(request):
    return render(request,'pages/home.html')

from django.shortcuts import render

def view_user_profile(request):
    return render(request, 'pages/profile.html')

