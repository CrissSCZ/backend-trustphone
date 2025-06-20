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
            tienda = Tienda.objects.get(id_tienda=usuario.tienda_id)
            if usuario.password == password: 
                request.session['user_id'] = str(usuario.id_usuario)
                request.session['user_email'] = usuario.email
                request.session['user_nombre'] = usuario.nombre
                request.session['user_rol'] = usuario.rol
                request.session['user_tienda'] = str(tienda.id_tienda)
                request.session['user_tienda_nombre'] = tienda.nombre
                request.session['user_tienda_imagen'] = tienda.fotografia.url
                return redirect('dashboard')
            else:
                error = 'Credenciales incorrectas'
        except Usuario.DoesNotExist:
            error = 'Usuario no encontrado'
        
        return render(request, 'modules/login/index.html', {
            'error': error,
            'email': email 
        })
    
    return render(request, 'modules/login/index.html')

def logout_view(request):
    request.session.flush()
    return redirect('login')

@login_required
def admin(request):
    tienda = Tienda.objects.get(id_tienda=request.session.get('user_tienda'))
    vendedores = Vendedor.objects.filter(tienda=tienda)
    print(vendedores)
    return render(request, 'modules/vendedores/index.html', {
        'vendedores': vendedores
    })
# Create your views here.
