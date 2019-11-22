from django.contrib import admin

# Register your models here.

from .models import Visitor, Registered_Customer, VIP_Customer

admin.site.register(Registered_Customer)
admin.site.register(VIP_Customer)