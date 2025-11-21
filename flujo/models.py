from django.db import models
from django.core.exceptions import ValidationError

class CotizacionDolar(models.Model):
    fecha = models.DateField(unique=True)
    valor = models.DecimalField(max_digits=10, decimal_places=2)  # Bs por USD
    class Meta:
        ordering = ['-fecha']
    def __str__(self):
        return f"{self.fecha} - {self.valor} Bs"

class MovimientoCaja(models.Model):
    MONEDAS = [('Bs','Bolívares'),('$','Dólares')]
    TIPO = [('Ingreso','Ingreso'),('Gasto','Gasto')]
    fecha = models.DateField()
    descripcion = models.CharField(max_length=200)
    tipo = models.CharField(max_length=10, choices=TIPO)
    monto = models.DecimalField(max_digits=15, decimal_places=2)
    moneda = models.CharField(max_length=2, choices=MONEDAS, default='Bs')
    monto_usd = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True)

    class Meta:
        ordering = ['-fecha']

    def save(self, *args, **kwargs):
        from decimal import Decimal
        if self.moneda == 'Bs':
            try:
                cot = CotizacionDolar.objects.get(fecha=self.fecha)
                self.monto_usd = Decimal(self.monto) / cot.valor
            except CotizacionDolar.DoesNotExist:
                raise ValidationError('No existe cotización para la fecha de este movimiento.')
        else:
            self.monto_usd = self.monto
        super().save(*args, **kwargs)

    def __str__(self):
        return f'{self.fecha} - {self.tipo} - {self.monto} {self.moneda} / {self.monto_usd} $'