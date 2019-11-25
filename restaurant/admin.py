from django.contrib import admin

from .models import Restaurant
from ratings.models import Rating
from cook.models import Cook
from delivery_person.models import DeliveryPerson


class RatingsInLine(admin.TabularInline):
    model = Rating
    classes = ['collapse', ]
    max_num = 10
    extra = 0


class CookInLine(admin.TabularInline):
    model = Cook
    classes = ['collapse', ]
    max_num = 3
    extra = 1


class DeliveryPersonInLine(admin.TabularInline):
    model = DeliveryPerson
    classes = ['collapse', ]
    max_num = 3
    extra = 1


class RestaurantAdmin(admin.ModelAdmin):
    inlines = (
        CookInLine,
        DeliveryPersonInLine,
        RatingsInLine,

    )

    fieldsets = ((None, {
        'fields': ('name', 'address', 'manager',),
        'classes': ('extrapretty'),
    }),)


admin.site.register(Restaurant, RestaurantAdmin)
