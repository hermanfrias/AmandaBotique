from django.db import models
from django.contrib.auth.models import AbstractUser


def cargar_avatar(instance, filename):
    return f"avatars/{instance.username}/{filename}"

class PerfilUsuario(AbstractUser):
    avatar = models.ImageField(upload_to = cargar_avatar, default = "default/default_icono.png", null=True, blank=True, verbose_name = "Avatar")
    ciudad = models.CharField(max_length=100, null=True, blank=True)
    pais = models.CharField(max_length=100, null=True, blank=True)
    telefono = models.CharField(max_length=20, null=True, blank=True)
    fecha_nacimiento = models.DateField(null=True, blank=True)
    
    class Meta:
        verbose_name = "Usuario"
        verbose_name_plural = "Usuarios"
        ordering = ['username']
    
    def __str__(self):
        return f"{self.username}: {self.last_name}, {self.first_name}"
    
        

