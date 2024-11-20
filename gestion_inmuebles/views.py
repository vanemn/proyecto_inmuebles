from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout # Para gestionar la autenticación de usuarios

# Create your views here.
def home(request):
    return render(request, 'home.html', {})

# Función para mostrar la página "Acerca de"
def about(request):
	return render(request, 'about.html', {})	

# Función para iniciar sesión del usuario
def login_user(request):
      return render(request, 'login.html', {})

# Función para cerrar sesión del usuario
def logout_user(request):
    pass