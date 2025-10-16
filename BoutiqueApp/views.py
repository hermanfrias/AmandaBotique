from django.shortcuts import render, redirect
from .forms import ClienteForm, CatalogoForm, ProveedorForm
from .models import Cliente, Catalogo, Proveedor

def index(request):
    return render(request, "BoutiqueApp/index.html")

def actualizar_catalogo(request):
    if request.method == 'POST':
        form = CatalogoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("actualizar_catalogo")
    else:
            form = CatalogoForm()
        
    return render(request, "BoutiqueApp/actualizar_catalogo.html", {'form': form})

def actualizar_clientes(request):
    if request.method == 'POST':
        form = ClienteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("actualizar_clientes")
    else:
            form = ClienteForm()
            
    return render(request, "BoutiqueApp/actualizar_clientes.html", {'form': form})

def actualizar_proveedores(request):
    if request.method == 'POST':
        form = ProveedorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("actualizar_proveedores")
    else:
            form = ProveedorForm()
            
    return render(request, "BoutiqueApp/actualizar_proveedores.html", {'form': form})

# --- LISTAR BASES DE DATOS ---

def listar_catalogo(request):
    query = request.GET.get('buscar', '')
    if len(query) > 0:
        catalogos = Catalogo.objects.filter(nombre__icontains=query).order_by('codigo')
    else:       
        catalogos = Catalogo.objects.all()
    return render(request, 'BoutiqueApp/listar_catalogo.html', {'catalogos': catalogos})

def listar_clientes(request):
    query = request.GET.get('buscar', '')
    if len(query) > 0:
        clientes = Cliente.objects.filter(nombre__icontains=query).order_by('identificacion ')
    else:       
        clientes = Cliente.objects.all()
    return render(request, 'BoutiqueApp/listar_clientes.html', {'clientes': clientes})

def listar_proveedores(request):
    query = request.GET.get('buscar', '')
    if len(query) > 0:
        proveedores = Proveedor.objects.filter(nombre__icontains=query).order_by('nombre')
    else:       
        proveedores = Proveedor.objects.all()
    return render(request, 'BoutiqueApp/listar_proveedores.html', {'proveedores': proveedores})

