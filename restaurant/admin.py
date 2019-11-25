from django.contrib import admin

from .models import Restaurant
from ratings.models import Rating
from cook.models import Cook
from delivery_person.models import DeliveryPerson
from salesperson.models import Salesperson
from item.models import Item
from customer.models import Customer


class CookInLine(admin.TabularInline):
    model = Cook
    classes = ['collapse', ]
    max_num = 3
    extra = 1

class CustomerInLine(admin.TabularInline):
    model = Customer
    classes = ['collapse', ]
    max_num = 3
    extra = 0


class DeliveryPersonInLine(admin.TabularInline):
    model = DeliveryPerson
    classes = ['collapse', ]
    max_num = 3
    extra = 1


class ItemsInLine(admin.TabularInline):
    model = Item
    classes = ['collapse', ]
    max_num = 3
    extra = 0


class RatingsInLine(admin.TabularInline):
    model = Rating
    classes = ['collapse', ]
    max_num = 10
    extra = 0


class SalesPersonInLine(admin.TabularInline):
    model = Salesperson
    classes = ['collapse', ]
    max_num = 3
    extra = 1


class RestaurantAdmin(admin.ModelAdmin):
    inlines = (
        CookInLine,
        DeliveryPersonInLine,
        SalesPersonInLine,
        ItemsInLine,
        CustomerInLine,
        RatingsInLine,
    )

    fieldsets = (('Contact Info', {
        'fields': ('name', 'address', 'manager',),
        'classes': ('extrapretty'),
    }),
        ('Data', {'fields': ()}),)


admin.site.register(Restaurant, RestaurantAdmin)
