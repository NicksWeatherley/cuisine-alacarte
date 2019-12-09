from django.urls import path

import ratings.views as view

urlpatterns = [
    # Path to rate something
    path('rate/customer/<int:customer_id>', view.RateCustomer, name = 'rate_customer'),
    path('rate/delivery/<int:delivery_id>', view.RateDelivery, name = 'rate_delivery'),
    path('rate/dish/<int:dish_id>', view.RateDish, name = 'rate_dish'),
    # path('rate/item/<int:item_id>', getItemRating, name = 'get_item_rating'),

    # Below is the paths to view all the different ratings
    path('ratings/Customer/<int:item_id>',
         view.CustomerRatingListView.as_view(), name='customer_rating_list'),
    path('ratings/Delivery/<int:item_id>',
         view.DeliveryRatingListView.as_view(), name='Delivery_rating_list'),
    path('ratings/Dish/<int:item_id>',
         view.DishRatingListView.as_view(), name='dish_rating_list'),
    path('ratings/Item/<int:item_id>',
         view.ItemRatingListView.as_view(), name='item_rating_list'),
]
