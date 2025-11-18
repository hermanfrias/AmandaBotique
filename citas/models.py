from django.db import models
from django.contrib.auth.models import User

class Cita(models.Model):
    ACCIONES = [
        ('toma_medidas', 'Toma de Medidas'),
        ('pruebas', 'Pruebas'),
        ('retiro', 'Retiro'),
        ('otros', 'Otros'),
    ]

    MONEDAS = [
        ('bs', 'Bs'),
        ('usd', '$'),
    ]

    cliente = models.CharField(max_length=100)
    fecha = models.DateField()
    hora = models.TimeField()
    descripcion = models.TextField(blank=True, null=True)
    medidas = models.CharField(max_length=100, blank=True, null=True)  # nuevo campo
    precio = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    abono = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    pago_total = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    moneda = models.CharField(max_length=3, choices=MONEDAS, default='bs')  # nuevo campo
    accion = models.CharField(max_length=20, choices=ACCIONES, default='otros')

    class Meta:
        ordering = ['fecha', 'hora']

    def __str__(self):
        return f"{self.cliente} - {self.fecha} {self.hora} ({self.get_accion_display()})"
