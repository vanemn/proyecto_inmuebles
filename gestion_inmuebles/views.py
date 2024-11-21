from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login, logout # Para gestionar la autenticación de usuarios
from django.contrib import messages # Para mostrar mensajes de notificación al usuario
from django.contrib.auth.models import User # Importa el modelo de usuario predeterminado de Django
from django.contrib.auth.forms import UserCreationForm # Importa el formulario de creación de usuarios predeterminado de Django
from .forms import SignUpForm # Importa formularios personalizados
from django import forms

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


# Función para registrar un nuevo usuario
def register_user(request):
	form = SignUpForm()
	if request.method == "POST":
		form = SignUpForm(request.POST)
		if form.is_valid():
			form.save()
			username = form.cleaned_data['username']
			password = form.cleaned_data['password1']
			# log in user
			user = authenticate(username=username, password=password)
			login(request, user)
			messages.success(request, ("Usuario registrado exitosamente..."))
			return redirect('update_info')
		else:
			messages.success(request, ("Whoops! hay un problema, intente nuevamente..."))
			return redirect('register')
	else:
		return render(request, 'register.html', {'form':form})

