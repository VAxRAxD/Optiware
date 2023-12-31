from django.urls import path
from . import dashboards,customers, manufacture, orders

urlpatterns = [
    path('dashboard/',dashboards.dashboard,name='dashboard'),
    path('store/',dashboards.store,name='store'),
    path('manufacture/',manufacture.listManufacturing,name='list_manufacture'),
    path('add_manufacture/',manufacture.startManufacturing,name='add_manufacture'),
    path('update_manufacture/',manufacture.updateStatus, name='update_manufacture'),
    path('add_customers/',customers.addCustomers, name="add_customer"),
    path('update_customers/',customers.updateCustomers, name='update_customer'),
    path('list_customers/', customers.listCustomers,name='list_customer'),
    path('list_orders/',orders.listOrders, name='list_orders')
]