from django import forms
from django.contrib.auth.forms import AuthenticationForm


class formulario_login(AuthenticationForm):
    username = forms.CharField(label=False, required=True, max_length=100, 
                            error_messages={'required':'Por favor complete su usuario'},
                            widget=forms.TextInput(attrs={'class':'cont-input', 'placeholder':'Ingrese su usuario'} ))
    password  = forms.CharField(label=False, required=True, max_length=100,
                            error_messages={'required':'Por favor ingrese su contraseña'},
                            widget=forms.PasswordInput(attrs={'class':'cont-input', 'placeholder':'Ingrese su contraseña'} ))


    class Meta:
        fields = ['username', 'password']