from django.urls import path

from .views import PurchaseListView

urlpatterns = [
    path('salesperson/purchaselist', PurchaseListView.as_view(), name='purchase_list'),
]
