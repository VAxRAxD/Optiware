from django.urls import path
from . import dashboards,customers, manufacture

urlpatterns = [
    path('dashboard/',dashboards.dashboard,name='dashboard'),
    path('store/',dashboards.store,name='store'),
    path('inventory/',dashboards.inventory,name='inventory'),
    path('manufacture/',manufacture.listManufacturing,name='list_manufacture'),
    path('add_manufacture/',manufacture.startManufacturing,name='add_manufacture'),
    path('update_manufacture/',manufacture.updateStatus, name='update_manufacture'),
    path('add/customers/',customers.customers, name="customers"),
    path('update/customers/',customers.updateCustomers),
    path('list_customers/', customers.listCustomers)
]