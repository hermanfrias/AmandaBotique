from django.contrib import admin
from .models import Cliente, Proveedor, Catalogo

# Register your models here.

@admin.register(Cliente)
class ClienteAdmin(admin.ModelAdmin):
    list_display = ('identificacion', 'nombre', 'apellido', 'email', 'telefono', 'fecha_creacion')
    search_fields = ('apellido', 'identificacion', 'email')
    list_filter = ('apellido', 'identificacion')
    ordering = ('nombre',)

@admin.register(Proveedor)
class ProveedorAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'contacto', 'telefono')
    search_fields = ('nombre', 'contacto')
    list_filter = ('nombre',)
    ordering = ('nombre',)

@admin.register(Catalogo)
class CatalogoAdmin(admin.ModelAdmin):
    list_display = ('codigo', 'nombre', 'descripcion', 'precio')
    search_fields = ('nombre',)
    list_filter = ('precio',)
    ordering = ('nombre',)

# Personalización del título y encabezado del admin
admin.site.site_header = "Administración de Amanda Boutique"
admin.site.site_title = "Panel de Administración de Amanda Boutique"
admin.site.index_title = "Bienvenido al Panel de Administración"

