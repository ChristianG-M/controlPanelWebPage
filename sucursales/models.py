from django.db import models
from django_countries.fields import CountryField
from django.contrib.auth.models import User

# Create your models here.
class Sucursal(models.Model):
    STATE_CHOICES = (
        ('Aguascalientes', 'Aguascalientes'), 
        ('Baja California', 'Baja California'), 
        ('Baja California Sur', 'Baja California Sur'), 
        ('Campeche', 'Campeche'), 
        ('Chihuahua', 'Chihuahua'), 
        ('Chiapas', 'Chiapas'), 
        ('Coahuila', 'Coahuila'), 
        ('Colima', 'Colima'), 
        ('CDMX', 'Ciudad de México'), 
        ('Durango', 'Durango'), 
        ('Guerrero', 'Guerrero'), 
        ('Guanajuato', 'Guanajuato'), 
        ('Hidalgo', 'Hidalgo'), 
        ('Jalisco', 'Jalisco'), 
        ('Estado de México', 'Estado de México'), 
        ('Michoacán', 'Michoacán'), 
        ('Morelos', 'Morelos'), 
        ('Nayarit', 'Nayarit'), 
        ('Nuevo León', 'Nuevo León'), 
        ('Oaxaca', 'Oaxaca'), 
        ('Puebla', 'Puebla'), 
        ('Querétaro', 'Querétaro'), 
        ('Quintana Roo', 'Quintana Roo'), 
        ('Sinaloa', 'Sinaloa'), 
        ('San Luis Potosí', 'San Luis Potosí'), 
        ('Sonora', 'Sonora'), 
        ('Tabasco', 'Tabasco'), 
        ('Tamaulipas', 'Tamaulipas'), 
        ('Tlaxcala', 'Tlaxcala'), 
        ('Veracruz', 'Veracruz'), 
        ('Yucatán', 'Yucatán'), 
        ('Zacatecas', 'Zacatecas')
    )
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