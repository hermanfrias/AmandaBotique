from django.contrib import admin
from .models import Catalogo
from LoginApp.models import PerfilUsuario

# Register your models here.

@admin.register(Catalogo)
class CatalogoAdmin(admin.ModelAdmin):
    list_display = ('codigo', 'modelo', 'estilo', 'descripcion', 'precio')
    search_fields = ('modelo',)
    list_filter = ('precio',)
    ordering = ('modelo',)
    
@admin.register(PerfilUsuario)
class CatalogoAdmin(admin.ModelAdmin):
    list_display = ('username', 'first_name', 'last_name')
    search_fields = ('username',)
    list_filter = ('last_name',)
    ordering = ('username',)

# Personalización del título y encabezado del admin
admin.site.site_header = "Administración de Amanda Boutique"
admin.site.site_title = "Panel de Administración de Amanda Boutique"
admin.site.index_title = "Bienvenido al Panel de Administración"

