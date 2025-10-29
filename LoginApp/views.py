from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from LoginApp.froms import FormularioCreacionUsuario, FormularioCambioUsuario

def registrar_usuario(request):
    if request.method == 'POST':
        form = FormularioCreacionUsuario(request.POST, request.FILES)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('perfil')
    else:
        form = FormularioCreacionUsuario()
    return render(request, 'LoginApp/registrar.html', {'form': form})

@login_required
def perfil(request):
    return(render(request, 'LoginApp/perfil.html', {'user':  request.user}))

@login_required
def editar_perfil(request):
    if request.method == 'POST':
        form = FormularioCambioUsuario(request.POST, request.FILES, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('editar_perfil')
    else:
        form = FormularioCambioUsuario(instance=request.user)
    return render(request, 'LoginApp/editar_perfil.html', {'form': form})




