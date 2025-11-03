from django import forms
from .models import Catalogo

class CatalogoForm(forms.ModelForm):
    class Meta:
        model = Catalogo
        fields = ['codigo','modelo', 'estilo', 'descripcion', 'precio', 'imagen_modelo']
        widgets = {
            "codigo": forms.TextInput(attrs={'class':'form-control'}),
            "nodelo": forms.TextInput(attrs={'class':'form-control'}),
            "estilo": forms.TextInput(attrs={'class':'form-control'}),
            "descripcion": forms.TextInput(attrs={'class':'form-control'}),
            "precio": forms.NumberInput(attrs={'class':'form-control'}),
            "imagen_modelo": forms.ClearableFileInput(attrs={"class": "form-control"}),
        }
        
