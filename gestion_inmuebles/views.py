from multiprocessing import context
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.models import User, Group
from .forms import SignUpForm, UpdateUserForm
from .models import Inmueble, Region, Comuna
from .forms import InmuebleSearchForm,Inmuebleform
from django.http import JsonResponse
from .models import Comuna




# Función para actualizar los datos del usuario
def update_user(request):
    if request.user.is_authenticated:
        current_user = User.objects.get(id=request.user.id)
        user_form = UpdateUserForm(request.POST or None, instance=current_user)

        if user_form.is_valid():
            user_form.save()
            login(request, current_user)
            messages.success(request, "Usuario ha sido actualizado!!")
            return redirect('home')
        return render(request, "update_user.html", {'user_form':user_form})
    
    else:
        messages.success(request, "debe iniciar sesion para acceder a esta página!!")  
        return redirect('home')
    


def get_comunas(request):
    region_id = request.GET.get('region_id')
    comunas = Comuna.objects.filter(region_id=region_id).values('id', 'nombre')
    return JsonResponse(list(comunas), safe=False)

# Vista principal que redirige según el tipo de usuario
#@login_required
def home(request):
    # Redirección según el tipo de usuario
    if request.user.is_authenticated:
        if request.user.groups.filter(name="Arrendador").exists():
            return redirect("arrendador_home")
        elif request.user.groups.filter(name="Vendedor").exists():
            return redirect("vendedor_home")
    
    # Formulario de búsqueda de inmuebles
    form = InmuebleSearchForm(request.GET or None)
    inmuebles = Inmueble.objects.all()

    if form.is_valid():
        if form.cleaned_data.get('region'):
            inmuebles = inmuebles.filter(region=form.cleaned_data['region'])
        if form.cleaned_data.get('comuna'):
            inmuebles = inmuebles.filter(comuna=form.cleaned_data['comuna'])
        if form.cleaned_data.get('dormitorios'):
            inmuebles = inmuebles.filter(dormitorios=form.cleaned_data['dormitorios'])
        if form.cleaned_data.get('baños'):
            inmuebles = inmuebles.filter(baños=form.cleaned_data['baños'])
#        if form.cleaned_data.get('tipo_inmueble'):
#            inmuebles = inmuebles.filter(tipo_inmueble=form.cleaned_data['tipo_inmueble'])
#        if form.cleaned_data.get('estado'):
#            inmuebles = inmuebles.filter(estado=form.cleaned_data['estado'])
#        if form.cleaned_data.get('precio_min'):
#            inmuebles = inmuebles.filter(precio_min__gte=form.cleaned_data['precio_min'])
#        if form.cleaned_data.get('precio_max'):
#            inmuebles = inmuebles.filter(precio_max__lte=form.cleaned_data['precio_max'])
#        if form.cleaned_data.get('fecha_inicio'):
#            inmuebles = inmuebles.filter(fecha_inicio__gte=form.cleaned_data['fecha_inicio'])
#        if form.cleaned_data.get('fecha_fin'):
#            inmuebles = inmuebles.filter(fecha_fin__lte=form.cleaned_data['fecha_fin'])

    return render(request, "home.html", {"form": form, "inmuebles": inmuebles})



# Vista para arrendadores
@login_required
def arrendador_home(request):
    return render(request, "arrendador_home.html", {})


# Vista para vendedores
@login_required
def vendedor_home(request):
        form = Inmuebleform()
        context = {
        "form" : form
        }
        return render (request,"vendedor_home.html",context)
#    return render(request, "vendedor_home.html", {})


# Vista para mostrar la página "Acerca de"
def about(request):
    return render(request, "about.html", {})


# Función para iniciar sesión del usuario
def login_user(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, "¡Ya ingresaste!")
            return redirect("home")
        else:
            messages.error(request, "Hay un error, intenta una vez más...")
            return redirect("login")
    else:
        return render(request, "registration/login.html", {})


# Función para cerrar sesión del usuario
def logout_user(request):
    logout(request)
    messages.success(request, "Ya hiciste logout, gracias por esta sesión...")
    return redirect("login")


# Función para registrar un nuevo usuario
def register_user(request):
    form = SignUpForm()
    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            user_type = form.cleaned_data["user_type"]

            # Asigna el grupo según el user_type
            if user_type == "arrendador":
                group = Group.objects.get(name="Arrendador")
            elif user_type == "vendedor":
                group = Group.objects.get(name="Vendedor")
            else:
                group = Group.objects.get(name="Usuario Normal")

            user.groups.add(group)
            user.save()

            username = form.cleaned_data["username"]
            password = form.cleaned_data["password1"]
            user = authenticate(username=username, password=password)
            login(request, user)
            messages.success(request, "Usuario registrado exitosamente.")
            return redirect("home")
        else:
            messages.error(request, "Error en el formulario. Intente nuevamente.")
            return redirect("register")
    else:
        return render(request, "register.html", {"form": form})


