from django import forms
from django import forms
from django.forms import ValidationError


class formulario_registro(forms.Form):
    nombre = forms.CharField(label=False, required=True, max_length=100, 
                            error_messages={'required':'Por favor complete su nombre'},
                            widget=forms.TextInput(attrs={'class':'cont-input', 'placeholder':'Ingrese su nombre'} ))
    apellido = forms.CharField(label=False, required=True, max_length=100, 
                            error_messages={'required':'Por favor complete su apellido'},
                            widget=forms.TextInput(attrs={'class':'cont-input', 'placeholder':'Ingrese su apellido'} ))
    mail = forms.EmailField(label=False, required=True,
                            error_messages={'required':'Por favor complete su Email'},
                            widget=forms.EmailInput(attrs={'class':'cont-input', 'placeholder':'Ingrese su Email'} ))
    contraseña_1  = forms.CharField(label=False, required=True, max_length=100,
                            error_messages={'required':'Por favor ingrese su contraseña'},
                            widget=forms.PasswordInput(attrs={'class':'cont-input', 'placeholder':'Ingrese su contraseña'} ))
    contraseña_2  = forms.CharField(label=False, required=True, max_length=100,
                            error_messages={'required':'Por favor ingrese su contraseña'},
                            widget=forms.PasswordInput(attrs={'class':'cont-input', 'placeholder':'Ingrese nuevamente su contraseña'} ))

    # Controla que las contraseñas introducidas sean iguales

    def clean(self):
        cleaned_data = super(formulario_registro, self).clean()
        password = cleaned_data.get("contraseña_1")
        confirm_password = cleaned_data.get("contraseña_2")

        if password != confirm_password:
            raise forms.ValidationError(
                "Las contraseñas ingresadas no coinciden"
            )
