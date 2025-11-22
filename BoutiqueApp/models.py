from django.db import models

class Catalogo(models.Model):
    codigo = models.CharField(max_length=20, unique=True, blank=True)
    modelo = models.CharField(max_length=100)
    estilo = models.CharField(max_length=100)
    descripcion = models.TextField(max_length=300)
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    imagen_modelo = models.ImageField(upload_to='imagenes', null=True)

    def save(self, *args, **kwargs):
        if not self.codigo:  # Si no tiene código, lo generamos
            ultimo = Catalogo.objects.all().order_by('codigo').last()
            if not ultimo:
                self.codigo = 'CAT00001'
            else:
                num = int(ultimo.codigo.replace('CAT', '')) + 1
                self.codigo = "CAT" + f"{num:05d}"
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.codigo}: {self.modelo} - {self.estilo}"



