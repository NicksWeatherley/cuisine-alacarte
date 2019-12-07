from django.urls import path

import ratings.views as view

urlpatterns = [
    path('ratings/Item/<int:item_id>', view.ItemRatingListView.as_view(), name='item_rating_list'),
]
