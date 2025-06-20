from django.shortcuts import render
from django.db.models import Sum
from django.utils.timezone import now
from apps.Ventas.models import Venta
from apps.Clientes.models import Cliente
from apps.Celulares.models import Celular
from apps.Vendedores.models import Vendedor
from apps.Usuarios.models import Usuario

def main(request):
    id_usuario = request.session.get('user_id')
    usuario = Usuario.objects.get(id_usuario=id_usuario)
    
    ventas = Venta.objects.filter(usuario=usuario)
    celulares = Celular.objects.filter(estado_venta=0, tienda=usuario.tienda)
    clientes = Cliente.objects.all()
    vendedores = Vendedor.objects.all()
    
    total_celulares = celulares.count()
    total_clientes = clientes.count()
    total_vendedores = vendedores.count()
    total_ventas = ventas.count()
    total_ventas_mes = ventas.aggregate(Sum('total'))['total__sum']
    
    return render(request, 'modules/dashboard/index.html', {'total_celulares': total_celulares, 'total_clientes': total_clientes, 'total_vendedores': total_vendedores, 'total_ventas_mes': total_ventas_mes, 'total_ventas': total_ventas, 'now': now()})
