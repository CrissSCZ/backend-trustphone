from django.shortcuts import render
from django.shortcuts import redirect
from apps.Tiendas.models import Tienda
from apps.Encargados.models import Encargado

def main(request):
    tienda = Tienda.objects.get(id_tienda=request.session.get('user_tienda'))
    encargado = Encargado.objects.get(id_encargado=tienda.encargado_id)
    
    if request.method == 'GET':
        return render(request, 'modules/configuracion/index.html', {'tienda': tienda, 'encargado': encargado})

    if request.method == 'POST':
        tienda.nombre = request.POST.get('nombre_tienda')
        tienda.direccion = request.POST.get('direccion_tienda')
        tienda.detalles = request.POST.get('detalles_tienda')
        if 'fotografia_tienda' in request.FILES:
            tienda.fotografia = request.FILES['fotografia_tienda']
        tienda.correo = request.POST.get('correo_tienda')
        tienda.save()
        
        encargado.nombre = request.POST.get('nombre_encargado')
        encargado.apellido = request.POST.get('apellido_encargado')
        encargado.telefono = request.POST.get('telefono_encargado')
        encargado.correo = request.POST.get('correo_encargado')
        encargado.carnet = request.POST.get('carnet_encargado')
        encargado.save()
        
        return redirect('configuracion')
