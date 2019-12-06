from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.template import loader
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required


# Create your views here.

def home(request):
    context = {
        'user' :request.user
    }
    return render(request,'pages/home.html', context)

from django.shortcuts import render

def view_user_profile(request):
    return render(request, 'pages/profile.html')

