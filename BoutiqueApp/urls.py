from django.urls import path
from .views import index
from . import views

urlpatterns = [
    path("", index, name="index"),
    path('actualizar_catalogo/', views.actualizar_catalogo, name='actualizar_catalogo'),
    path('actualizar_clientes/', views.actualizar_clientes, name='actualizar_clientes'),
    path('actualizar_proveedores/', views.actualizar_proveedores, name='actualizar_proveedores'),
    path('listar_catalogo/', views.listar_catalogo, name='listar_catalogo'),
    path('listar_clientes/', views.listar_clientes, name='listar_clientes'),
    path('listar_proveedores/', views.listar_proveedores, name='listar_proveedores'),
]

