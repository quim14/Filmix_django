from django import forms
from django.forms import TextInput, Textarea, FileInput
from .models import Funcion
from .models import Pelicula
from django.forms import ValidationError

class PeliculaForm(forms.ModelForm):

    class Meta:
        model=Pelicula
        fields=['nombre', 'descripcion', 'trailer','poster']
        widgets = {
            'nombre': TextInput(attrs={'class': 'form-control', 'placeholder': 'Nombre de la pelicula', 'required' : 'true',}),
            'descripcion': Textarea(attrs={'class': 'form-control','placeholder': 'Descripcion de la pelicula','rows': 5,}),
            'trailer': TextInput(attrs={'class': 'form-control','placeholder': 'Ej: https://www.youtube.com/embed/...',}),
            'poster': FileInput(attrs={'class': 'form-control'}),
        }
        error_messages = {
            'nombre':{
                'required':'Por favor ingrese el nombre'
            }
        }
    # nombre = forms.CharField(label='Nombre', required=True, max_length=100,
    #                         error_messages={'required':'Por favor ingrese el nombre de la pelicula'},
    #                         widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nombre de la pelicula', 'required' : 'true',}))
    # descripcion = forms.CharField(label='Descripcion',
    #                             required=True,
    #                             error_messages={'required':'Por favor complete con la descripcion'},
    #                             widget=forms.Textarea(attrs={
    #                                 'class': 'form-control',
    #                                 'placeholder': 'Descripcion de la pelicula',
    #                                 'rows': 5,}))
    # trailer = forms.CharField(label='URL del Trailer',
    #                         required=True, max_length=150,
    #                         error_messages={'required':'Por favor complete con el trailer'},
    #                         widget=forms.TextInput(attrs={
    #                             'class': 'form-control',
    #                             'placeholder': 'Ej: https://www.youtube.com/embed/...',}))
                            
    # poster = forms.ImageField(label='Poster',
    #                         required=False,
    #                         widget=forms.FileInput(attrs={'class': 'form-control'}))

    def clean(self):
        cleaned_data = super(PeliculaForm, self).clean()
        nombre = cleaned_data.get("nombre")
        if nombre!=" ":
            raise forms.ValidationError("Nombre inválido")

    # imagen = forms.FileField(
    #     label='Poster',
    #     widget=forms.ClearableFileInput(attrs={
    #         'class': 'form-control form-control-sm',
    #         'required' : 'true',
    #     }))

    # def clean(self):
    #     cleaned_data = super(PeliculaForm,self).clean()
    #     nombre = cleaned_data.get("nombre")
    #     descripcion = cleaned_data.get("descripcion")
    #     if nombre!='' and descripcion != '':
    #         raise forms.ValidationError("Debe ingresar el nombre y descripcion")

class PeliculaFormValidado(PeliculaForm):
    def clean_nombre(self):
        data = self.cleaned_data["nombre"]
        if data == ' ':
            raise ValidationError('Nombre no valido')
        return data
    

class FuncionesForm(forms.Form):
    fecha = forms.DateField(
        label='Fecha',
        required=True,
        widget=forms.DateInput(attrs={'class':'form-control', 'type':'date'})
    )
    pelicula = forms.ModelChoiceField(label="Pelicula",
        required=True,
        queryset=Pelicula.objects.filter(baja=False),
        widget=forms.Select(attrs={'class':'form-control'}))

class HorarioForm(forms.Form):
    hora = forms.TimeField(
        label='Hora',
        required=True,
        widget=forms.DateInput(attrs={'class':'form-control', 'type':'time'})
    )




