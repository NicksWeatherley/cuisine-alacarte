from django.urls import path

from .views import DishListView

urlpatterns = [
    path('cook/dishlist', DishListView.as_view(), name='dish_list'),
]


