from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView
from django.urls import reverse, reverse_lazy
from .models import Sucursal

# Create your views here.
class SucursalListView(ListView):
    model = Sucursal

class SucursalDetailView(DetailView):
    model = Sucursal

class SucursalCreate(CreateView):
    model = Sucursal
    fields = [
        'nombre',
        'empresa',
        'latitud',
        'longitud',
        'pais',
        'estado',
        'alcaldia',
        'codigoPostal',
        'colonia',
        'calle',
        'numero',
        'telefono',
        'correo',
        'horaApertura',
        'horaCierre',
        'image',
        'supervisor'        
    ]
    success_url = reverse_lazy('Sucursal:Sucursales')