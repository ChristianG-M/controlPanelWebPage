from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.admin.views.decorators import staff_member_required
from django.utils.decorators import method_decorator
from django.urls import reverse, reverse_lazy
from django.shortcuts import redirect
from .models import Sucursal
from .forms import SucursalForm

#Mixin para validar que es miembro del staff
class StaffRequiredMixin(object):
    @method_decorator(staff_member_required)
    def dispatch(self, request, *args, **kwargs):
        return super(StaffRequiredMixin, self).dispatch(request, *args, **kwargs)


# Create your views here.
@method_decorator(staff_member_required, name='dispatch')
class SucursalListView(ListView):
    model = Sucursal

@method_decorator(staff_member_required, name='dispatch')
class SucursalDetailView(DetailView):
    model = Sucursal

@method_decorator(staff_member_required, name='dispatch')
class SucursalCreate(CreateView):
    model = Sucursal
    form_class = SucursalForm
    success_url = reverse_lazy('Sucursal:Sucursales')    

@method_decorator(staff_member_required, name='dispatch')
class SucursalUpdate(UpdateView):
    model = Sucursal
    form_class = SucursalForm
    template_name_suffix = '_update_form'

    def get_success_url(self):
        return reverse_lazy('Sucursal:Update', args=[self.object.id]) + '?ok'

@method_decorator(staff_member_required, name='dispatch')
class SucursalDelete(DeleteView):
    model = Sucursal
    success_url = reverse_lazy('Sucursal:Sucursales')