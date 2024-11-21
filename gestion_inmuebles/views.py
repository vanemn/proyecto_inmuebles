from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login, logout # Para gestionar la autenticación de usuarios
from django.contrib import messages # Para mostrar mensajes de notificación al usuario

# Create your views here.
def home(request):
    return render(request, 'home.html', {})

# Función para mostrar la página "Acerca de"
def about(request):
	return render(request, 'about.html', {})	

# Función para iniciar sesión del usuario
def login_user(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, "¡Ya ingresaste!")
            return redirect('home')
        else:
            messages.error(request, "Hay un error, intenta una vez más...")
            return redirect('login')
    else:
        return render(request, 'login.html', {})

# Función para cerrar sesión del usuario
def logout_user(request):
	logout(request)
	messages.success(request, ("ya hiciste logout, gracias por esta sesión..."))
	return redirect('home')