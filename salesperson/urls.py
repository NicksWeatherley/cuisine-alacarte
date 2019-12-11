from django.urls import path

from .views import PurchaseListView, EditCommission

urlpatterns = [
    path('salesperson/purchaselist',
        PurchaseListView.as_view(), name='purchase_list'),
    path('salesperson/commission/<int:salesperson_id>',
        EditCommission, name='edit_commission'),
]
