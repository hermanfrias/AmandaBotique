from django import forms
from .models import Cita
from datetime import date

class CitaForm(forms.ModelForm):
    class Meta:
        model = Cita
        fields = [
            'cliente','fecha','hora','descripcion','busto', 'cintura','largo','otra',
            'precio','abono','pago_total','moneda','accion', 'fecha_entrega'
        ]
        widgets = {
            'cliente': forms.TextInput(attrs={'class':'form-control'}),
            'fecha': forms.DateInput(attrs={'type':'date','class':'form-control'}, format ='%Y-%m-%d',),
            'fecha_entrega': forms.DateInput(attrs={'type':'date','class':'form-control'}, format ='%Y-%m-%d'),
            'hora': forms.TimeInput(attrs={'type':'time','class':'form-control'}),
            'descripcion': forms.Textarea(attrs={'class':'form-control','rows':3}),
            'busto': forms.TextInput(attrs={'class':'form-control'}),
            'cintura': forms.TextInput(attrs={'class':'form-control'}),
            'largo': forms.TextInput(attrs={'class':'form-control'}),
            'otra': forms.TextInput(attrs={'class':'form-control'}),
            'precio': forms.NumberInput(attrs={'class':'form-control'}),
            'abono': forms.NumberInput(attrs={'class':'form-control'}),
            'pago_total': forms.NumberInput(attrs={'class':'form-control'}),
            'moneda': forms.Select(attrs={'class':'form-select'}),
            'accion': forms.Select(attrs={'class':'form-select'}),
        }

