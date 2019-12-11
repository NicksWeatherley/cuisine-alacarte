from django.contrib import admin
from .models import Cook
from item.models import Dish


class DishInLine(admin.TabularInline):
    model = Dish
    classes = ['collapse', ]
    max_num = 3


class CookAdmin(admin.ModelAdmin):
    inlines = [
        DishInLine,
    ]


admin.site.register(Cook, CookAdmin)
