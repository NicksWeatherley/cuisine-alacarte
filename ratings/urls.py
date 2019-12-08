from django.urls import path

import ratings.views as view

urlpatterns = [
    path('ratings/Customer/<int:item_id>',
         view.CustomerRatingListView.as_view(), name='customer_rating_list'),
    path('ratings/Delivery/<int:item_id>',
         view.DeliveryRatingListView.as_view(), name='Delivery_rating_list'),
    path('ratings/Dish/<int:item_id>',
         view.DishRatingListView.as_view(), name='dish_rating_list'),
    path('ratings/Item/<int:item_id>',
         view.ItemRatingListView.as_view(), name='item_rating_list'),
]
