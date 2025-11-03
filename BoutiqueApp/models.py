from django.db import models

class Catalogo(models.Model):
    codigo = models.CharField(max_length=20, unique=True)
    modelo = models.CharField(max_length=100)
    estilo = models.CharField(max_length=100)
    descripcion = models.TextField()
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    imagen_modelo = models.ImageField(upload_to = 'imagenes', null=True, blank = True)
        
    def __str__(self):
        return f"{self.codigo}: {self.modelo} - {self.estilo}"
    

    

