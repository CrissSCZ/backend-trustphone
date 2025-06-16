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
        tienda.nombre = request.POST.get('nombre')
        tienda.direccion = request.POST.get('direccion')
        tienda.detalles = request.POST.get('detalles')
        tienda.fotografia = request.POST.get('fotografia')
        tienda.correo = request.POST.get('correo')
        tienda.save()
        
        encargado.nombre = request.POST.get('nombre')
        encargado.apellido = request.POST.get('apellido')
        encargado.telefono = request.POST.get('telefono')
        encargado.correo = request.POST.get('correo')
        encargado.carnet = request.POST.get('carnet')
        encargado.save()
        
        return redirect('configuracion')
