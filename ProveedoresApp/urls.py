from django.urls import path
from ProveedoresApp.views import *

urlpatterns = [
    path('', ProveedoresListView.as_view(), name='proveedores_list'),
    path('crear/', ProveedoresCreateView.as_view(), name='proveedores_create'),
    path('<int:pk>/editar/', ProveedoresUpdateView.as_view(), name='proveedores_update'),
    path('<int:pk>/eliminar/', ProveedoresDeleteView.as_view(), name='proveedores_delete'),
    path('<int:pk>/', ProveedoresDetailView.as_view(), name='proveedores_detail'),
]
