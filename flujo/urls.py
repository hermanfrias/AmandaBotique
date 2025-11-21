from django.urls import path
from . import views

urlpatterns = [
    path('', views.listar_movimientos, name='listar_movimientos'),
    path('movimientos/crear/', views.crear_movimiento, name='crear_movimiento'),
    path('cotizaciones/', views.listar_cotizaciones, name='listar_cotizaciones'),
    path('cotizaciones/crear/', views.crear_cotizacion, name='crear_cotizacion'),
    path('dashboard/', views.dashboard_flujo, name='dashboard_flujo'),
]