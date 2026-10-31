from django.contrib import admin
from .models import Shipment

class ShipmentAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'get_excerpt', 'created_date')

admin.site.register(Shipment, ShipmentAdmin)