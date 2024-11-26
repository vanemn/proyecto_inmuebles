from django.urls import path, include  # Asegúrate de importar 'include'
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('get_comunas/', views.get_comunas, name='get_comunas'),
    path('about/', views.about, name='about'),
    path('login/', views.login_user, name='login'),
    path('logout/', views.logout_user, name='logout'),
    path('register/', views.register_user, name='register'),
    path('vendedor_home/', views.vendedor_home, name='vendedor_home'),
    path('arrendador_home/', views.arrendador_home, name='arrendador_home'),
    #path('accounts/', include('django.contrib.auth.urls')),  # Incluir URLs de autenticación
]
