from django.contrib import admin

from .models import DeliveryPerson, Delivery

class DeliveryInLine(admin.TabularInline):
    model = Delivery
    extra = 0
    max_num = 5

class DeliverPersonAdmin(admin.ModelAdmin):
    fields = ('first_name', 'last_name', 'ssn', 'salary','restaurant')

    inlines = [
        DeliveryInLine,
    ]

admin.site.register(DeliveryPerson, DeliverPersonAdmin)