from django.contrib import admin

# Register your models here.

from .models import Customer, Order


class OrderInLine(admin.TabularInline):
    model = Order
    classes = ['collapse', ]
    max_num = 3
    extra = 0

class CustomerAdmin(admin.ModelAdmin):
    inlines = [
        OrderInLine,
    ]

admin.site.register(Customer, CustomerAdmin)
admin.site.register(Order)
