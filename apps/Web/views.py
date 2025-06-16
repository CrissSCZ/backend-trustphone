from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from apps.Usuarios.models import Usuario
from apps.Vendedores.models import Vendedor
from apps.Tiendas.models import Tienda

def login_view(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        
        try:
            usuario = Usuario.objects.get(email=email)
            tienda = Tienda.objects.get(id=usuario.tienda_id)
            if usuario.password == password: 
                request.session['user_id'] = str(usuario.id_usuario)
                request.session['user_email'] = usuario.email
                request.session['user_nombre'] = usuario.nombre
                request.session['user_rol'] = usuario.rol
                request.session['user_tienda'] = str(tienda.id_tienda)
                return redirect('administrador')
            else:
                error = 'Credenciales incorrectas'
        except Usuario.DoesNotExist:
            error = 'Usuario no encontrado'
        
        return render(request, 'modules/login/index.html', {'error': error})
    
    return render(request, 'modules/login/index.html')

def logout_view(request):
    request.session.flush()
    return redirect('login')

@login_required
def admin(request):
    # # Verificar si el usuario tiene una tienda asignada
    # user_tienda = request.session.get('user_tienda')
    # if user_tienda:
    #     # Si es vendedor, mostrar solo los productos de su tienda
    #     if request.session.get('user_rol') == 'vendedor':
    #         marcas = Marca.objects.filter(tienda__id=user_tienda)
    #     else:
    #         marcas = Marca.objects.all()
    # else:
    #     marcas = Marca.objects.all()
    tienda = Tienda.objects.get(id_tienda=request.session.get('user_tienda'))
    vendedores = Vendedor.objects.filter(tienda=tienda)
    print(vendedores)
    return render(request, 'modules/vendedores/index.html', {
        'vendedores': vendedores
    })
# Create your views here.
