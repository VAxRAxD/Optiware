from django.urls import path
from . import dashboards,customers

urlpatterns = [
    path('dashboard/',dashboards.dashboard,name="dashboard"),
    path('',dashboards.store,name='store'),
    path('add/customers/',customers.customers, name="customers"),
    path('update/customers/',customers.updateCustomers),
    path('list_customers/', customers.listCustomers)
]