from django import forms
from django import forms

class formulario_registro(forms.Form):
    nombre = forms.CharField(label='Ingrese su nombre', required=True, max_length=100)
    apellido = forms.CharField(label='Ingrese su apellido', required=True, max_length=100)
    mail = forms.EmailField(label="Ingrese su Email", required=True)
    contraseña_1  = forms.CharField(label='Ingrese su contraseña', required=True, max_length=100)
    contraseña_2  = forms.CharField(label='Ingrese nuevamente su contraseña', required=True, max_length=100)