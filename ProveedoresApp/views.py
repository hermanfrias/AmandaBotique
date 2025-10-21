from ProveedoresApp.forms import ProveedorForm
from ProveedoresApp.models import Proveedores
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView

# Create your views here.

class ProveedoresListView(ListView):
    model = Proveedores
    template_name = 'proveedores_list.html'
    context_object_name = 'proveedores'
           
    def get_queryset(self):
        query = self.request.GET.get('buscar', '')
        if query:
            return Proveedores.objects.filter(nombre=query).order_by('codigo_proveedor')
        return Proveedores.objects.all()
    
class ProveedoresCreateView(CreateView):
    model = Proveedores
    form_class = ProveedorForm
    template_name = 'ProveedoresApp/proveedores_create.html'
    success_url = reverse_lazy('proveedores_list')  
    
class ProveedoresUpdateView(UpdateView):
    model = Proveedores
    form_class = ProveedorForm
    template_name = 'proveedores_create.html'
    success_url = reverse_lazy('proveedores_list')
    slug_field = 'key_api'
    slug_url_kwarg = 'key_api'
    
class ProveedoresDeleteView(DeleteView):
    model = Proveedores
    template_name = 'proveedores_confirm_delete.html'
    success_url = reverse_lazy('proveedores_list')
    slug_field = 'key_api'
    slug_url_kwarg = 'key_api'
    
class ProveedoresDetailView(DetailView):
    model = Proveedores
    template_name = 'proveedores_detail.html'
    context_object_name = 'proveedor'
    slug_field = 'key_api'
    slug_url_kwarg = 'key_api'
    
    
    