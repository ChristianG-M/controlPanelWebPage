from django import forms
from .models import Sucursal

class SucursalForm(forms.ModelForm):

    class Meta:
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
        widgets = {
            'nombre': forms.TextInput(attrs={'class':'form-control', 'placeholder': 'Nombre'}),
            'empresa': forms.TextInput(attrs={'class':'form-control', 'placeholder': 'Empresa'}),
            'latitud': forms.NumberInput(attrs={'class':'form-control', 'placeholder': 'Latitud'}),
            'longitud': forms.NumberInput(attrs={'class':'form-control', 'placeholder': 'Longitud'}),
            'pais': forms.Select(attrs={'class':'form-control', 'placeholder': 'Pais'}),
            'estado': forms.Select(attrs={'class':'form-control', 'placeholder': 'Estado'}),
            'alcaldia': forms.TextInput(attrs={'class':'form-control', 'placeholder': 'Alcaldia'}),
            'codigoPostal': forms.TextInput(attrs={'class':'form-control', 'placeholder': 'Código Postal'}),
            'colonia': forms.TextInput(attrs={'class':'form-control', 'placeholder': 'Colonia'}),
            'calle': forms.TextInput(attrs={'class':'form-control', 'placeholder': 'Calle'}),
            'numero': forms.NumberInput(attrs={'class':'form-control', 'placeholder': 'Número'}),
            'telefono': forms.TextInput(attrs={'class':'form-control', 'placeholder': 'Telefono'}),
            'correo': forms.EmailInput(attrs={'class':'form-control', 'placeholder': 'Correo'}),
            'horaApertura': forms.TimeInput(attrs={'class':'form-control', 'placeholder': 'Hora de Apertura'}),
            'horaCierre': forms.TimeInput( format='%H:%M:%S', attrs={'class':'form-control', 'placeholder': 'Hora de Cierre'}),
            'image': forms.FileInput(attrs={'class':'form-control'}),
            'supervisor': forms.Select(attrs={'class':'form-control', 'placeholder':'Supervisor'}),
        }
        labels = {
            'nombre':'',
            'empresa':'',
            'latitud':'',
            'longitud':'',
            'pais':'Pais',
            'estado':'Estado',
            'alcaldia':'',
            'codigoPostal':'',
            'colonia':'',
            'calle':'',
            'numero':'',
            'telefono':'',
            'correo':'',
            'horaApertura':'',
            'horaCierre':'',
            'image':'Imagen',
            'supervisor':'',
        }