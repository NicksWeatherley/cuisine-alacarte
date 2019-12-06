from django.urls import path

from salesperson.views import PurchaseListView, purchase_detail

urlpatterns = [
    path('salesperson/purchaselist', PurchaseListView.as_view(), name='purchase_list'),
    path('salesperson/purchasedetail/<int:purchase_id>', purchase_detail, name='purchase_detail'),
]
