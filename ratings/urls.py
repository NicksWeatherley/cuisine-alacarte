from django.urls import path

from .views import RatingListView

urlpatterns = [
    path('ratings/customerlist', RatingListView.as_view(), name='rating_list'),
]
