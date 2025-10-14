from django.shortcuts import render
from .models import Cliente, Catalogo, Proveedor

# Create your views here.
def index(request):
    return render(request, "Botique/index.html")

def actualizar_catalogo(request):
    # Lógica para actualizar el catálogo
    return render(request, "Botique/actualizar_catalogo.html")

def actualizar_clientes(request):
    # Lógica para actualizar los clientes
    return render(request, "Botique/actualizar_clientes.html")

def actualizar_proveedores(request):
    # Lógica para actualizar los proveedores
    return render(request, "Botique/actualizar_proveedores.html")

# --- LISTAR BASES DE DATOS ---

def listar_catalogo(request):
    catalogo = Catalogo.objects.all()
    return render(request, 'Botique/listar_catalogo.html', {'productos': catalogo})

def listar_clientes(request):
    clientes = Cliente.objects.all()
    return render(request, 'Botique/listar_clientes.html', {'clientes': clientes})

def listar_proveedores(request):
    proveedores = Proveedor.objects.all()
    return render(request, 'Botique/listar_proveedores.html', {'proveedores': proveedores})


