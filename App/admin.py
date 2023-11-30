from django.contrib import admin
from . models import *

admin.site.register(Product)
admin.site.register(RawMaterial)
admin.site.register(Supplier)
admin.site.register(Warehouse)
admin.site.register(Inventory)
admin.site.register(Customer)
admin.site.register(Order)
admin.site.register(Purchase)
admin.site.register(Manufacturing)