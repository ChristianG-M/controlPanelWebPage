from django.db import models
from django_countries.fields import CountryField
from django.contrib.auth.models import User

# Create your models here.
class Sucursales(models.Model):
    STATE_CHOICES = (('AGU', 'Aguascalientes'), ('BCN', 'Baja California'), ('BCS', 'Baja California Sur'), ('CAM', 'Campeche'), ('CHH', 'Chihuahua'), ('CHP', 'Chiapas'), ('COA', 'Coahuila'), ('COL', 'Colima'), ('CDMX', 'Ciudad de México'), ('DUR', 'Durango'), ('GRO', 'Guerrero'), ('GUA', 'Guanajuato'), ('HID', 'Hidalgo'), ('JAL', 'Jalisco'), ('MEX', 'Estado de México'), ('MIC', 'Michoacán'), ('MOR', 'Morelos'), ('NAY', 'Nayarit'), ('NLE', 'Nuevo León'), ('OAX', 'Oaxaca'), ('PUE', 'Puebla'), ('QUE', 'Querétaro'), ('ROO', 'Quintana Roo'), ('SIN', 'Sinaloa'), ('SLP', 'San Luis Potosí'), ('SON', 'Sonora'), ('TAB', 'Tabasco'), ('TAM', 'Tamaulipas'), ('TLA', 'Tlaxcala'), ('VER', 'Veracruz'), ('YUC', 'Yucatán'), ('ZAC', 'Zacatecas'))
    id = models.AutoField(primary_key=True, verbose_name="ID")
    nombre = models.CharField(max_length=255, verbose_name="Nombre")
    empresa = models.CharField(max_length=255, verbose_name="Empresa")
    latitud = models.FloatField(verbose_name="Latitud")
    longitud = models.FloatField(verbose_name="Longitud")
    pais = CountryField()
    estado = models.CharField(max_length=255, choices=STATE_CHOICES, verbose_name="Estado")
    alcaldia = models.CharField(max_length=255, verbose_name="Alcaldia")
    codigoPostal = models.CharField(max_length=10, verbose_name="Código Postal")
    colonia = models.CharField(max_length=255, verbose_name="Colonia")
    calle = models.CharField(max_length=255, verbose_name="Calle")
    numero = models.PositiveIntegerField(verbose_name="Número")
    telefono = models.CharField(max_length=15, verbose_name="Teléfono")
    correo = models.EmailField(verbose_name="Correo", blank=True, null=True)
    horaApertura = models.TimeField(verbose_name="Hora de Apertura")
    horaCierre = models.TimeField(verbose_name="Hora de Cierre")
    image = models.ImageField(verbose_name="Imagen", upload_to="sucursales", null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación")
    lastUpdate = models.DateTimeField(auto_now=True, verbose_name="Fecha de Modificación")
    supervisor = models.ForeignKey(User, verbose_name="Supervisor", on_delete=models.CASCADE)

    class Meta:
        verbose_name = "Sucursal"
        verbose_name_plural = "Sucursales"
        ordering = ['id']

    def __str__(self):
        return self.nombre