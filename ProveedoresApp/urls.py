from django.urls import path
from ProveedoresApp.views import *

urlpatterns = [
    path('', ProveedoresListView.as_view(), name='proveedores_list'),
    path('crear/', ProveedoresCreateView.as_view(), name='proveedores_create'),
    path('<str:codigo_proveedor>/editar/', ProveedoresUpdateView.as_view(), name='proveedores_update'),
    path('<str:codigo_proveedor>/eliminar/', ProveedoresDeleteView.as_view(), name='proveedores_confirm_delete'),
    path('<str:codigo_proveedor>/', ProveedoresDetailView.as_view(), name='proveedores_detail'),
    
]
