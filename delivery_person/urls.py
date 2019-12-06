from django.urls import path

from .views import DeliveryListView

urlpatterns = [
    path('deliveryperson/deliverylist', DeliveryListView.as_view(), name='delivery_list'),
]
