from django.urls import path
from .views import index
from . import views

urlpatterns = [
    path("", index, name="index"),
    path('actualizar_catalogo/', views.actualizar_catalogo, name='actualizar_catalogo'),
    path('listar_catalogo/', views.listar_catalogo, name='listar_catalogo'),
    path('ver_catalogo/<str:codigo>/', views.detalle_catalogo, name='detalle_catalogo'),
    path('editar_catalogo/<str:codigo>/', views.editar_catalogo, name='editar_catalogo'),
    path('eliminar_catalogo/<str:codigo>/', views.eliminar_catalogo, name='eliminar_catalogo'),
]

