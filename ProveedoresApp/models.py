from django.db import models
import uuid

# Create your models here.
def generar_key_api():
    import uuid
    return uuid.uuid4().hex

class Proveedores(models.Model):
    codigo_proveedor = models.CharField(max_length=20, unique=True) 
    nombre = models.CharField(max_length=100)
    contacto = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    telefono = models.CharField(max_length=15)
    direccion = models.TextField()
    rublo = models.CharField(max_length=100)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    key_api = models.CharField(max_length=32, 
        default=generar_key_api,
        unique=True)

    def __str__(self):
        return f"{self.nombre} - {self.rublo}"