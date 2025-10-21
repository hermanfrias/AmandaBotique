from django import forms
from .models import Cliente, Catalogo

class ClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = ['identificacion','nombre', 'apellido', 'email', 'telefono', 'direccion', 'fecha_nacimiento']
        widgets = {
            "identificacion": forms.TextInput(attrs={'class':'form-control'}),
            "nombre": forms.TextInput(attrs={'class':'form-control'}),
            "apellido": forms.TextInput(attrs={'class':'form-control'}),
            "email": forms.EmailInput(attrs={'class':'form-control'}),
            "telefono": forms.TextInput(attrs={'class':'form-control'}), 
            "direccion": forms.Textarea(attrs={'class':'form-control'}),
            "fecha_nacimiento": forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),        
        }
        
class CatalogoForm(forms.ModelForm):
    class Meta:
        model = Catalogo
        fields = ['codigo','nombre', 'descripcion', 'precio']
        widgets = {
            "codigo": forms.TextInput(attrs={'class':'form-control'}),
            "nombre": forms.TextInput(attrs={'class':'form-control'}),
            "descripcion": forms.TextInput(attrs={'class':'form-control'}),
            "precio": forms.NumberInput(attrs={'class':'form-control'}),
        }
        
