from django.contrib import admin

from .models import Salesperson, Purchase


class PurchaseInLine(admin.TabularInline):
    model = Purchase
    extra = 1
    max_num = 5
    classes = ['collapse', ]


class SalespersonAdmin(admin.ModelAdmin):
    inlines = [
        PurchaseInLine,
    ]

    fieldsets = ((
        'data', {
            'fields': (
                'first_name',
                'last_name',
                 'ssn',
                 'salary',
                 'restaurant',
                 )
        }
    ),)


admin.site.register(Salesperson, SalespersonAdmin)
