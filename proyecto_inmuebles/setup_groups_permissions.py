# en la consola de shell

from django.contrib.auth.models import Group, Permission
from django.contrib.contenttypes.models import ContentType
from gestion_inmuebles.models import Inmueble

# Crear grupo Arrendador
arrendador_group, created = Group.objects.get_or_create(name="Arrendador")
arrendador_perms = ["add_inmueble", "view_inmueble"]
for perm in arrendador_perms:
    permission = Permission.objects.get(
        codename=perm, content_type=ContentType.objects.get_for_model(Inmueble)
    )
    arrendador_group.permissions.add(permission)

# Crear grupo Vendedor
vendedor_group, created = Group.objects.get_or_create(name="Vendedor")
vendedor_perms = ["add_inmueble", "change_inmueble", "view_inmueble"]
for perm in vendedor_perms:
    permission = Permission.objects.get(
        codename=perm, content_type=ContentType.objects.get_for_model(Inmueble)
    )
    vendedor_group.permissions.add(permission)

# Crear grupo Usuario Normal
usuario_normal_group, created = Group.objects.get_or_create(name="Usuario Normal")
usuario_normal_perms = ["view_inmueble"]
for perm in usuario_normal_perms:
    permission = Permission.objects.get(
        codename=perm, content_type=ContentType.objects.get_for_model(Inmueble)
    )
    usuario_normal_group.permissions.add(permission)

print("Grupos y permisos creados y asignados correctamente.")
