from django.contrib import admin
from .models import Sucursal

# Register your models here.
class SucursalAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'lastUpdate')

admin.site.register(Sucursal, SucursalAdmin)