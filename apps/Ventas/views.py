from django.shortcuts import render, redirect
from apps.Ventas.models import Venta
from apps.Ventas.models import Detalle_Venta
from django.db.models.query import Prefetch
from apps.Celulares.models import Celular
from apps.Clientes.models import Cliente
from apps.Usuarios.models import Usuario

def main(request):
    id_usuario = request.session.get('user_id')
    ventas = Venta.objects.prefetch_related(
        Prefetch('detalle_venta_set', queryset=Detalle_Venta.objects.select_related('celular'))
    ).select_related('cliente', 'usuario').filter(usuario=id_usuario)
    
    return render(request, 'modules/ventas/index.html', {'ventas': ventas})

def crear_venta(request):
    if request.method == 'POST':
        id_cliente=request.POST.get('cliente')
        email_usuario = request.session['user_email']
        cliente = Cliente.objects.get(id_cliente=id_cliente)
        usuario = Usuario.objects.get(email=email_usuario)
        venta = Venta.objects.create(
            cliente=cliente,
            usuario=usuario,
            descuento = 0,
            total = 0
        )
        for id_celular in request.POST.getlist('celulares'):
            celular = Celular.objects.get(id_celular=id_celular)
            Detalle_Venta.objects.create(
                venta=venta,
                celular=celular,
                precio_unitario=celular.precio,
            )
            celular.estado_venta = 1
            celular.save()
            venta.total += celular.precio
        venta.save()
        generar_recibo(request, venta.id_venta)
        return redirect('ventas')
    
    celulares = Celular.objects.filter(estado_venta=0)
    clientes = Cliente.objects.all()
    usuario = Usuario.objects.get(email=request.session['user_email'])
    
    return render(request, 'modules/ventas/crear_venta.html', {'celulares': celulares, 'clientes': clientes})

def generar_recibo(request, id_venta):
    venta = Venta.objects.get(id_venta=id_venta)
    detalles = Detalle_Venta.objects.select_related('celular').filter(venta=venta)
    return render(request, 'modules/ventas/recibo.html', {
        'venta': venta,
        'detalles': detalles
    })

