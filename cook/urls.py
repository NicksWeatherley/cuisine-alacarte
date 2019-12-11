from django.urls import path

from .views import DishListView, get_new_dish, get_dishes_to_remove

urlpatterns = [
    path('cook/dishlist', DishListView.as_view(), name='dish_list'),
    path('cook/adddish/<int:cook_id>', get_new_dish, name='get_new_dish'),
    path('cook/getdishestoremove/<int:cook_id>', get_dishes_to_remove, name='get_dishes_to_remove' )
]

