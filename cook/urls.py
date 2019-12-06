from django.urls import path

from . import views

urlpatterns = [
    path('cook_menu/', views.view_cook_menu, name='cook_menu'),
]

