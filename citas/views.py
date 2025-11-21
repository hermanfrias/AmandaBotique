from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.http import JsonResponse
from django.utils.dateformat import format
from .models import Cita
from .forms import CitaForm

# @login_required
# def listar_citas(request):
#     query = request.GET.get('buscar', '')
#     if len(query) > 0:
#         citas = Cita.objects.filter(cliente__icontains=query).order_by('cliente')
#     else:       
#         citas = Cita.objects.all()
#     return render(request, 'citas/listar_citas.html', {'citas': citas})
@login_required
def listar_citas(request):
    # Búsqueda por cliente
    query = request.GET.get('buscar', '')
    citas = Cita.objects.all()
    
    if query:
        citas = citas.filter(cliente__icontains=query)

    # Orden dinámico por GET
    orden = request.GET.get('orden', '')
    if orden == "fecha":
        citas = citas.order_by("fecha")
    elif orden == "-fecha":
        citas = citas.order_by("-fecha")
    elif orden == "entrega":
        citas = citas.order_by("fecha_entrega")
    elif orden == "-entrega":
        citas = citas.order_by("-fecha_entrega")
    else:
        citas = citas.order_by("cliente")  # Orden por defecto

    return render(request, 'citas/listar_citas.html', {'citas': citas})


@login_required
def crear_cita(request):
    if request.method=='POST':
        form=CitaForm(request.POST)
        if form.is_valid():
            cita=form.save(commit=False)
            cita.creado_por=request.user
            cita.save()
            messages.success(request,"Cita creada correctamente")
            return redirect('listar_citas')
    else:
        form=CitaForm()
    return render(request,'citas/crear_cita.html',{'form':form})

@login_required
def editar_cita(request, pk):
    cita=get_object_or_404(Cita, pk=pk)
    if request.method=='POST':
        form=CitaForm(request.POST, instance=cita)
        if form.is_valid():
            form.save()
            messages.success(request,"Cita actualizada correctamente")
            return redirect('listar_citas')
    else:
        form=CitaForm(instance=cita)
    return render(request,'citas/editar_cita.html',{'form':form})

@login_required
def eliminar_cita(request, pk):
    cita=get_object_or_404(Cita, pk=pk)
    if request.method=='POST':
        cita.delete()
        return redirect('listar_citas')
    return render(request,'citas/eliminar_cita.html',{'cita':cita})

def ver_cita(request, pk):
    cita = get_object_or_404(Cita, pk=pk)
    return render(request, 'citas/ver_cita.html', {'cita': cita})

@login_required
def calendario_citas(request):
    return render(request, 'citas/calendario.html')


@login_required
def eventos_citas(request):
    from django.urls import reverse
    
    citas = Cita.objects.all()
    eventos = []

    for c in citas:
        # Evento de fecha de cita (color rosa)
        eventos.append({
            "title": f"{c.cliente} - {c.get_accion_display()}",
            "start": str(c.fecha),
            "color": "#E91E63",
            "url": reverse("ver_cita", args=[c.pk])  # 👈
        })

        # Evento de fecha de entrega (color morado)
        if c.fecha_entrega:
            eventos.append({
                "title": f"Entrega: {c.cliente}",
                "start": str(c.fecha_entrega),
                "color": "#6A1B9A",
                "url": reverse("ver_cita", args=[c.pk])  # 👈
            })

    return JsonResponse(eventos, safe=False)
