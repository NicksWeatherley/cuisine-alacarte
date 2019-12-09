from django.urls import path

from .views import DeliveryListView, get_bid

urlpatterns = [
    path('deliveryperson/deliverylist', DeliveryListView.as_view(), name='delivery_list'),
    path('deliveryperson/bid/<int:purchase_id>', get_bid, name='get_bid')
]

