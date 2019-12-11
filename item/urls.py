from django.urls import path

from .views import ItemListView

urlpatterns = [
    path('item/cook_viewlist', ItemListView.as_view() , name='view_cook_item_list'),
]
