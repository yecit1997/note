from django import forms
from .models import Nota


class NotaForm(forms.ModelForm):
    class Meta:
        model = Nota
        fields = ['titulo', 'contenido']
        widgets = {
            'titulo': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Título de la nota', 'id': 'titulo'}),
            'contenido': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Contenido de la nota', 'id': 'contenido'}),
        }
        labels = {
            'titulo': '',
            'contenido': '',
        }
       