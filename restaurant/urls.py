from django.urls import path

from .views import RestaurantListView

urlpatterns = [
    path('restaurant/restaurantlist', RestaurantListView.as_view(), name='restaurant_list'),
]

