from django.urls import path
from .views import SucursalListView, SucursalDetailView, SucursalCreate, SucursalUpdate, SucursalDelete

sucursal_patterns = ([
    path('', SucursalListView.as_view(), name="Sucursales"),
    path('<int:pk>/',SucursalDetailView.as_view(), name="Sucursal"),
    path('create/', SucursalCreate.as_view(), name="Create"),
    path('update/<int:pk>/', SucursalUpdate.as_view(), name="Update"),
    path('delete/<int:pk>/', SucursalDelete.as_view(), name="Delete"),
], 'Sucursal')