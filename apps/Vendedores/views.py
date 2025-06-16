from django.shortcuts import render
from django.shortcuts import redirect
from .models import Vendedor

def main(request):
    return render(request, 'modules/vendedores/index.html', {'vendedores': Vendedor.objects.all()})

def crear_vendedor(request):
    if request.method == 'POST':
        nombre = request.POST['nombres']
        apellido = request.POST['apellidos']
        telefono = request.POST['telefono']
        correo = request.POST['correo']
        activo = True
        Vendedor.objects.create(nombre=nombre, apellido=apellido, telefono=telefono, correo=correo, activo=activo)
        return redirect('vendedores')
    else:
        if request.method == "GET":
            return render(request, 'modules/vendedores/crear_vendedor.html')
        else:
            return redirect('vendedores')


def editar_vendedor(request, id_vendedor):
    vendedor = Vendedor.objects.get(id_vendedor=id_vendedor)
    if request.method == 'POST':
        nombre = request.POST['nombres'] 
        apellido = request.POST['apellidos']
        telefono = request.POST['telefono']
        correo = request.POST['correo']
        activo = True
        vendedor.nombre = nombre
        vendedor.apellido = apellido
        vendedor.telefono = telefono
        vendedor.correo = correo
        vendedor.activo = activo
        vendedor.save()
        return redirect('vendedores')
    else:
        if request.method == "GET":
            return render(request, 'modules/vendedores/editar_vendedor.html', {'vendedor': vendedor})
        else:
            return redirect('vendedores')

def eliminar_vendedor(request, id_vendedor):
    vendedor = Vendedor.objects.get(id_vendedor=id_vendedor)
    vendedor.delete()
    return redirect('vendedores')
# Create your views here.
