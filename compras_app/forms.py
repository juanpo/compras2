from django import forms

class CrearForm(forms.Form):
    codigo = forms.CharField(label='Codigo', max_length=7)
    descripcion = forms.CharField(label="Descripcion", max_length=100)