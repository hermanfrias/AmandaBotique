from django.shortcuts import render, redirect
from .forms import ClienteForm, CatalogoForm
from .models import Cliente, Catalogo

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

# --- VER DETALLES DE LOS REGISTROS ---

def detalle_catalogo(request, codigo):
    catalogo = Catalogo.objects.get(codigo=codigo)
    return render(request, 'BoutiqueApp/detalle_catalogo.html', {'catalogo': catalogo})

# --- EDITAR LOS REGISTROS ---

def editar_catalogo(request, codigo):
    catalogo = Catalogo.objects.get(codigo=codigo)
    if request.method == 'POST':
        form = CatalogoForm(request.POST, instance=catalogo)
        if form.is_valid():
            form.save()
            return redirect('listar_catalogo')
    else:
        form = CatalogoForm(instance=catalogo)
    return render(request, 'BoutiqueApp/editar_catalogo.html', {'form': form})

# --- ELIMINAR UN REGISTROS ---

def eliminar_catalogo(request, codigo):
    catalogo = Catalogo.objects.get(codigo=codigo)
    if request.method == 'POST':
        catalogo.delete()
        return redirect('listar_catalogo')
    return render(request, 'BoutiqueApp/eliminar_catalogo.html', {'catalogo': catalogo})


