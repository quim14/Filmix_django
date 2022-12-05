from django import forms

class PeliculaForm(forms.Form):
    nombre = forms.CharField(
        label='Nombre',
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Nombre de la pelicula',
            'required' : 'true',
        }))
    descripcion = forms.CharField(
        required=False,
        widget=forms.Textarea(attrs={
            'class': 'form-control',
            'placeholder': 'Descripcion de la pelicula',
            'rows': 5,
            'required' : 'false',
        }))
    trailer = forms.CharField(
        label='URL del Trailer', 
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Ej: https://www.youtube.com/embed/...',
            'required' : 'false',

        }))
    imagen = forms.FileField(
        label='Poster',
        widget=forms.ClearableFileInput(attrs={
            'class': 'form-control form-control-sm',
            'required' : 'true',
        }))

    # def clean(self):
    #     cleaned_data = super(PeliculaForm,self).clean()
    #     nombre = cleaned_data.get("nombre")
    #     descripcion = cleaned_data.get("descripcion")
    #     if nombre!='' and descripcion != '':
    #         raise forms.ValidationError("Debe ingresar el nombre y descripcion")


class FuncionesForm(forms.Form):
    fecha = forms.DateField(
        label='Fecha',
        widget=forms.DateInput(attrs={'class':'form-control', 'type':'date'})
    )
    horario = forms.TimeField(
        label='Horario',
        widget=forms.TimeInput(attrs={'class':'form-control', 'type':'time'})
    )
    cantidad = forms.CharField(
        label='Cantidad',
        widget=forms.NumberInput(attrs={'class':'form-control', 'max':'10', 'min':'0'})
    )






