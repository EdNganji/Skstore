from django.contrib import admin
from .models import Brand
from .models import Item

class ItemAdmin(admin.ModelAdmin):
    readonly_fields = ('Brand',)

admin.site.register(Brand)
admin.site.register(Item, ItemAdmin)
