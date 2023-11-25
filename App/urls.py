from django.urls import path
from . import dashboards,manufacture

urlpatterns = [
    path('dashboard/',dashboards.dashboard,name='dashboard'),
    path('store/',dashboards.store,name='store'),
    path('inventory/',dashboards.inventory,name='inventory'),
    path('manufacture/',manufacture.listManufacturing,name='list_manufacture'),
    path('add_manufacture/',manufacture.startManufacturing,name='add_manufacture'),
    path('update_manufacture/',manufacture.updateStatus, name='update_manufacture'),
]