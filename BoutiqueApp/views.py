from django.shortcuts import render, redirect
from BoutiqueApp.forms import CatalogoForm
from BoutiqueApp.models import Catalogo
from django.contrib.auth.decorators import login_required

def index(request):
    catalogos = Catalogo.objects.all()
    return render(request, 'BoutiqueApp/index.html', {'catalogos': catalogos})

def actualizar_catalogo(request):
    if request.method == 'POST':
        form = CatalogoForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect("actualizar_catalogo")
    else:
            form = CatalogoForm()
        
    return render(request, "BoutiqueApp/actualizar_catalogo.html", {'form': form})

# --- LISTAR BASES DE DATOS ---

@login_required
def listar_catalogo(request):
    query = request.GET.get('buscar', '')
    if len(query) > 0:
        catalogos = Catalogo.objects.filter(modelo__icontains=query).order_by('modelo')
    else:       
        catalogos = Catalogo.objects.all()
    return render(request, 'BoutiqueApp/listar_catalogo.html', {'catalogos': catalogos})

# --- VER DETALLES DE LOS REGISTROS ---

@login_required
def detalle_catalogo(request, codigo):
    catalogo = Catalogo.objects.get(codigo=codigo)
    return render(request, 'BoutiqueApp/detalle_catalogo.html', {'catalogo': catalogo})

# --- EDITAR LOS REGISTROS ---

@login_required
def editar_catalogo(request, codigo):
    catalogo = Catalogo.objects.get(codigo=codigo)
    if request.method == 'POST':
        form = CatalogoForm(request.POST, request.FILES, instance=catalogo )
        if form.is_valid():
            form.save()
            return redirect('listar_catalogo')
    else:
        form = CatalogoForm(instance=catalogo)
    return render(request, 'BoutiqueApp/editar_catalogo.html', {'form': form})

# --- ELIMINAR UN REGISTROS ---

@login_required
def eliminar_catalogo(request, codigo):
    catalogo = Catalogo.objects.get(codigo=codigo)
    if request.method == 'POST':
        catalogo.delete()
        return redirect('listar_catalogo')
    return render(request, 'BoutiqueApp/eliminar_catalogo.html', {'catalogo': catalogo})
