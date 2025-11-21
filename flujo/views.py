import io
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.core.exceptions import ValidationError
from django.db.models import Sum
from django.db.models.functions import TruncMonth
from .models import MovimientoCaja, CotizacionDolar
from .forms import MovimientoCajaForm, CotizacionDolarForm

@login_required
def listar_movimientos(request):
    movimientos = MovimientoCaja.objects.all()
    return render(request, 'flujo/listar_movimientos.html', {'movimientos': movimientos})

@login_required
def crear_movimiento(request):
    if request.method=='POST':
        form = MovimientoCajaForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                messages.success(request,'Movimiento guardado correctamente')
                return redirect('listar_movimientos')
            except ValidationError as e:
                form.add_error('fecha', e)
    else:
        form = MovimientoCajaForm()
    return render(request,'flujo/crear_movimiento.html',{'form':form})

@login_required
def listar_cotizaciones(request):
    cotizaciones = CotizacionDolar.objects.all()
    return render(request,'flujo/listar_cotizaciones.html',{'cotizaciones':cotizaciones})

@login_required
def crear_cotizacion(request):
    if request.method=='POST':
        form = CotizacionDolarForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,'Cotización guardada correctamente')
            return redirect('listar_cotizaciones')
    else:
        form = CotizacionDolarForm()
    return render(request,'flujo/crear_cotizacion.html',{'form':form})

@login_required
def dashboard_flujo(request):
    movimientos = MovimientoCaja.objects.all()
    total_ingresos_usd = movimientos.filter(tipo='Ingreso').aggregate(total=Sum('monto_usd'))['total'] or 0
    total_gastos_usd = movimientos.filter(tipo='Gasto').aggregate(total=Sum('monto_usd'))['total'] or 0
    saldo_usd = total_ingresos_usd - total_gastos_usd

    total_ingresos_bs = 0
    total_gastos_bs = 0
    for m in movimientos:
        if m.moneda == 'Bs':
            factor = 1
        else:
            try:
                cot = CotizacionDolar.objects.get(fecha=m.fecha)
                factor = cot.valor
            except CotizacionDolar.DoesNotExist:
                factor = 1
        if m.tipo == 'Ingreso':
            total_ingresos_bs += m.monto_usd * factor
        else:
            total_gastos_bs += m.monto_usd * factor
    saldo_bs = total_ingresos_bs - total_gastos_bs

    meses=[]
    ingresos_mes=[]
    gastos_mes=[]
    queryset=movimientos.annotate(mes=TruncMonth('fecha')).values('mes').order_by('mes').distinct()
    for q in queryset:
        mes=q['mes'].strftime('%B %Y')
        meses.append(mes)
        ingresos_mes.append(round(movimientos.filter(tipo='Ingreso',fecha__month=q['mes'].month,fecha__year=q['mes'].year).aggregate(total=Sum('monto_usd'))['total'] or 0,2))
        gastos_mes.append(round(movimientos.filter(tipo='Gasto',fecha__month=q['mes'].month,fecha__year=q['mes'].year).aggregate(total=Sum('monto_usd'))['total'] or 0,2))

    context={
        'total_ingresos_usd': round(total_ingresos_usd,2),
        'total_gastos_usd': round(total_gastos_usd,2),
        'saldo_usd': round(saldo_usd,2),
        'total_ingresos_bs': round(total_ingresos_bs,2),
        'total_gastos_bs': round(total_gastos_bs,2),
        'saldo_bs': round(saldo_bs,2),
        'meses': meses,
        'ingresos_mes': ingresos_mes,
        'gastos_mes': gastos_mes
    }

    return render(request,'flujo/dashboard.html',context)


