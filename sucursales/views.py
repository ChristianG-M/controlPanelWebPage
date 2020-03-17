from django.shortcuts import render, get_object_or_404, get_list_or_404
from .models import Sucursales

# Create your views here.
def sucursales(request):
    sucursales = get_list_or_404(Sucursales)
    return render(request, "sucursales/sucursales.html", {'sucursales':sucursales})

def sucursal(request, sucursal_id, sucursal_slug):
    sucursal = get_object_or_404(Sucursales, id=sucursal_id)
    return render(request, "sucursales/sucursal.html", {'sucursal':sucursal})    