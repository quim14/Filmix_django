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
        label='Trailer', 
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'URL de Youtube del trailer',
        }))
    imagen = forms.FileField(
        label='Poster',
        widget=forms.ClearableFileInput(attrs={
            'class': 'form-control form-control-sm'
        }))





