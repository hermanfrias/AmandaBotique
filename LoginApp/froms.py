from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from LoginApp.models import PerfilUsuario

class FormularioCreacionUsuario(UserCreationForm):
    class Meta:
        model = PerfilUsuario
        fields = ('username', 'email', 'avatar')
        
class FormularioCambioUsuario(UserChangeForm):
    class Meta:
        model = PerfilUsuario
        fields = ('avatar', 'ciudad', 'pais', 'telefono', 'fecha_nacimiento', 'first_name', 'last_name', 'password', 'username')
        
        Widget = {
            "avatar": forms.ClearableFileInput(attrs={"class": "form-control"}),
            "pais": forms.TextInput(attrs={"class": "form-control", "placeholder": "País"}),
            "ciudad": forms.TextInput(attrs={"class": "form-control", "placeholder": "Ciudad"}),
            "first_name": forms.TextInput(attrs={"class": "form-control", "placeholder": "Nombre"}),
            "last_name": forms.TextInput(attrs={"class": "form-control", "placeholder": "Apellido"}),
            "username": forms.TextInput(attrs={"class": "form-control", "placeholder": "Nombre de usuario"}),
            "password": forms.PasswordInput(attrs={"class": "form-control", "readonly": "readonly"}),
        }
        
        
        