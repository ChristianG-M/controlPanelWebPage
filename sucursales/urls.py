from django.urls import path
from .views import SucursalListView, SucursalDetailView, SucursalCreate

sucursal_patterns = ([
    path('', SucursalListView.as_view(), name="Sucursales"),
    path('<int:pk>/',SucursalDetailView.as_view(), name="Sucursal"),
    path('create/', SucursalCreate.as_view(), name="Create")
], 'Sucursal')