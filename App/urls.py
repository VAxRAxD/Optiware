from django.urls import path
from . import dashboards

urlpatterns = [
    path('dashboard/',dashboards.dashboard,name="dashboard"),
    path('',dashboards.store,name='store'),
]