from django.urls import path

import customer.views as view
from .views import get_dishes_to_order, view_shopping_cart

urlpatterns = [
    path('customer/history', view.CustomerListView.as_view(), name='view_history'),
    path('customer/createorder', get_dishes_to_order, name='get_dishes_to_order'),
    path('customer/shoppingcart', view_shopping_cart, name='view_shopping_cart')
]

