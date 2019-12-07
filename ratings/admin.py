from django.contrib import admin

import ratings.models as mod
# from item.models import Item, Dish

admin.site.register(mod.ItemRating)
admin.site.register(mod.DishRating)
admin.site.register(mod.CustomerRating)
admin.site.register(mod.CookRating)