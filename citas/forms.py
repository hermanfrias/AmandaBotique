from django import forms
from .models import Cita
from datetime import date

class CitaForm(forms.ModelForm):
    class Meta:
        model = Cita
        fields = [
            'cliente','fecha','hora','descripcion','medidas',
            'precio','abono','pago_total','moneda','accion'
        ]
        widgets = {
            'cliente': forms.TextInput(attrs={'class':'form-control'}),
            'fecha': forms.DateInput(attrs={'type':'date','class':'form-control'}),
            'hora': forms.TimeInput(attrs={'type':'time','class':'form-control'}),
            'descripcion': forms.Textarea(attrs={'class':'form-control','rows':3}),
            'medidas': forms.TextInput(attrs={'class':'form-control'}),
            'precio': forms.NumberInput(attrs={'class':'form-control'}),
            'abono': forms.NumberInput(attrs={'class':'form-control'}),
            'pago_total': forms.NumberInput(attrs={'class':'form-control'}),
            'moneda': forms.Select(attrs={'class':'form-select'}),
            'accion': forms.Select(attrs={'class':'form-select'}),
        }

