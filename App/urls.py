from django.urls import path
from . import dashboards,customers, manufacture, orders, purchase, forecast, camera, tests, cctvserver

urlpatterns = [
    path('dashboard/',dashboards.dashboard,name='dashboard'),
    path('history/',dashboards.history,name='history'),
    path('store/',dashboards.store,name='store'),
    path('manufacture/',manufacture.listManufacturing,name='list_manufacture'),
    path('add_manufacture/',manufacture.startManufacturing,name='add_manufacture'),
    path('update_manufacture/',manufacture.updateStatus, name='update_manufacture'),
    path('add_customers/',customers.addCustomers, name="add_customer"),
    path('update_customers/',customers.updateCustomers, name='update_customer'),
    path('list_customers/', customers.listCustomers,name='list_customer'),
    path('list_orders/',orders.listOrders, name='list_orders'),
    path('place_order/',orders.placeOrder,name='place_order'),
    path('list_purchase/', purchase.listPurchase,name='list_purchase'),
    path('purchase/',purchase.purchaseRawMaterial,name='purchase_material'),
    path('forecast/',forecast.getForecast, name='forecast'),
    path('cctv/', cctvserver.index, name='index'),
    path('warehouse_feed/', cctvserver.warehouse_feed, name='warehouse_feed'),
    path('machinery_feed/', cctvserver.machinery_feed, name='machinery_feed'),
]