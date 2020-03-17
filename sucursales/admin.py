from django.contrib import admin
from .models import Sucursales

# Register your models here.
class SucursalesAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'lastUpdate')

admin.site.register(Sucursales, SucursalesAdmin)