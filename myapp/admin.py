from django.contrib import admin
from .models import InventoryItem

@admin.register(InventoryItem)
class InventoryItemAdmin(admin.ModelAdmin):
    list_display = ['title', 'icon_class']
    list_editable = ['icon_class']

admin.site.site_header = "EBENEZER LLC Admin"
admin.site.site_title = "EBENEZER LLC Admin Portal"
admin.site.index_title = "Welcome to EBENEZER LLC Admin Portal"