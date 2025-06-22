from django.shortcuts import render, redirect
from .models import Marca, Celular
from apps.Vendedores.models import Vendedor
from apps.Tiendas.models import Tienda

def main(request):
    tienda_id = request.session.get('user_tienda')
    celulares = Celular.objects.filter(tienda=tienda_id, estado_venta=0)
    return render(request, 'modules/celulares/index.html', {'celulares': celulares})

def crear_celular(request):
    vendedores = Vendedor.objects.filter(activo=True)
    marcas = Marca.objects.filter(activo=True)
    if request.method == 'POST':
        modelo = request.POST['modelo']
        color = request.POST['color']
        ram = int(request.POST['ram'])
        almacenamiento = int(request.POST['almacenamiento'])
        estado = int(request.POST['estado'])
        detalles = request.POST['detalles']
        imei = request.POST['imei']
        imei2 = request.POST.get('imei2', None)
        precio_base = float(request.POST['precio_base'])
        marca_id = request.POST['marca']
        vendedor_id = request.POST['vendedor']
        tienda_id = request.session.get('user_tienda')
        imagen = request.FILES.get('imagenes')
        
        print("tienda id",tienda_id)
        print("vendedor id",vendedor_id)
        print("marca id",marca_id)
        try:
            marca = Marca.objects.get(id_marca=marca_id)
            vendedor = Vendedor.objects.get(id_vendedor=vendedor_id)
            tienda = Tienda.objects.get(id_tienda=tienda_id)

            Celular.objects.create(
                modelo=modelo,
                color=color,
                almacenamiento=almacenamiento,
                ram=ram,
                estado=estado,
                detalles=detalles,
                imei=imei,
                imei2=imei2,
                precio_base=precio_base,
                precio_minimo=precio_base,
                precio=precio_base + 80,
                imagenes=imagen,
                marca=marca,
                tienda=tienda,
                vendedor=vendedor,
                activo=True
            )
            return redirect('celulares')
        except (Tienda.DoesNotExist, Marca.DoesNotExist, Vendedor.DoesNotExist, ValueError):
            return redirect('error')
    else:
        return render(request, 'modules/celulares/crear_celular.html', {
            'vendedores': vendedores,
            'marcas': marcas
        })

def editar_celular(request, id_celular):
    celular = Celular.objects.get(id_celular=id_celular)
    vendedores = Vendedor.objects.filter(activo=True)
    marcas = Marca.objects.filter(activo=True)
    if request.method == 'POST':
        celular.modelo = request.POST['modelo']
        celular.color = request.POST['color']
        celular.ram = int(request.POST['ram'])
        celular.almacenamiento = int(request.POST['almacenamiento'])
        celular.estado = int(request.POST['estado'])
        celular.detalles = request.POST['detalles']
        celular.imei = request.POST['imei']
        celular.imei2 = request.POST.get('imei2', None)
        celular.precio_base = float(request.POST['precio_base'])
        celular.marca_id = request.POST['marca']
        celular.vendedor_id = request.POST['vendedor']
        celular.tienda_id = request.session.get('user_tienda')
        celular.imagenes = request.FILES.get('imagenes')
        celular.save()
        return redirect('celulares')
    else:
        return render(request, 'modules/celulares/editar_celular.html', {
            'celular': celular,
            'vendedores': vendedores,
            'marcas': marcas
        })

def eliminar_celular(request, id_celular):
    celular = Celular.objects.get(id_celular=id_celular)
    celular.delete()
    return redirect('celulares')
