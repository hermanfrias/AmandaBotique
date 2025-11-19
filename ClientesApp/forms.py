from django import forms
from ClientesApp.models import Clientes

class ClientesForm(forms.ModelForm):
    class Meta:
        model = Clientes
        fields = ['identificacion','nombre', 'apellido', 'email', 'telefono', 'direccion']
        widgets = {
            "identificacion": forms.TextInput(attrs={'class':'form-control'}),
            "nombre": forms.TextInput(attrs={'class':'form-control'}),
            "apellido": forms.TextInput(attrs={'class':'form-control'}),
            "email": forms.EmailInput(attrs={'class':'form-control'}),
            "telefono": forms.TextInput(attrs={'class':'form-control'}), 
            "direccion": forms.Textarea(attrs={'class':'form-control'}),
        }
        