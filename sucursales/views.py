from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse, reverse_lazy
from .models import Sucursal
from .forms import SucursalForm

# Create your views here.
class SucursalListView(ListView):
    model = Sucursal

class SucursalDetailView(DetailView):
    model = Sucursal

class SucursalCreate(CreateView):
    model = Sucursal
    form_class = SucursalForm
    success_url = reverse_lazy('Sucursal:Sucursales')

class SucursalUpdate(UpdateView):
    model = Sucursal
    form_class = SucursalForm
    template_name_suffix = '_update_form'

    def get_success_url(self):
        return reverse_lazy('Sucursal:Update', args=[self.object.id]) + '?ok'

class SucursalDelete(DeleteView):
    model = Sucursal
    success_url = reverse_lazy('Sucursal:Sucursales')