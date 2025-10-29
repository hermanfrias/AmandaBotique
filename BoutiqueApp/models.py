from django.db import models

# Create your models here.
class Catalogo(models.Model):
    codigo = models.CharField(max_length=20, unique=True)
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    precio = models.DecimalField(max_digits=10, decimal_places=2)
        
    def __str__(self):
        return f"{self.codigo}: {self.nombre}"
    
class Cliente(models.Model):
    identificacion = models.CharField(max_length=20, unique=True)
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    telefono = models.CharField(max_length=15)
    direccion = models.TextField()
    fecha_nacimiento = models.DateField()
    fecha_creacion = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.identificacion}: {self.apellido}, {self.nombre}"
    

