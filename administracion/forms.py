from django import forms

class PeliculaForm(forms.Form):
    nombre = forms.CharField(
        label='Nombre',
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Nombre de la pelicula'
        }))
    descripcion = forms.CharField(
        required=False,
        widget=forms.Textarea(attrs={
            'class': 'form-control',
            'placeholder': 'Descripcion de la pelicula',
            'rows': 5,
        }))
    trailer = forms.CharField(
        label='URL del Trailer', 
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Ej: https://www.youtube.com/embed/...',
        }))
    imagen = forms.FileField(
        label='Poster',
        widget=forms.ClearableFileInput(attrs={
            'class': 'form-control form-control-sm'
        }))


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






