from django.urls import path
from .views import HomePageView

urlpatterns = [
    path('',HomePageView.as_view(), name="Inicio"),
    path('administracion/',HomePageView.as_view(), name="Administracion"),
    path('cortes/',HomePageView.as_view(), name="Cortes"),
    path('estadisticas/',HomePageView.as_view(), name="Estadisticas"),
    path('equipos/',HomePageView.as_view(), name="Equipos"),
    path('reportes/',HomePageView.as_view(), name="Reportes"),
    path('sucursal/',HomePageView.as_view(), name="Sucursal"),
    path('usuarios/',HomePageView.as_view(), name="Usuarios"),    
]