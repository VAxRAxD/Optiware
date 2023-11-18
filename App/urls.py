from django.urls import path
from . import dashboards,orders

urlpatterns = [
    path('dashboard/',dashboards.dashboard,name="dashboard"),
    path('store/',dashboards.store,name='store'),
    path('manufacture/',orders.startManufacturing,name='manufacturing')
]