from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('profile/', views.view_user_profile, name='profile'),

]
