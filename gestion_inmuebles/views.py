from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'home.html', {})

# Función para mostrar la página "Acerca de"
def about(request):
	return render(request, 'about.html', {})	