# Importa los modelos y formularios necesarios de Django y otros módulos
from django.contrib.auth.models import (
    User,
)  # Importa el modelo de usuario predeterminado de Django
from django.contrib.auth.forms import (
    UserCreationForm,
)  # Importa formularios de creación y cambio de usuario y formulario para establecer contraseña
from django import forms  # Importa el módulo de formularios de Django
from .models import Region, Comuna

# Define un formulario personalizado para el registro de nuevos usuarios
class SignUpForm(UserCreationForm):
    # Define los campos adicionales para el formulario
    email = forms.EmailField(
        label="",
        widget=forms.TextInput(
            attrs={"class": "form-control", "placeholder": "Email Address"}
        ),
    )
    first_name = forms.CharField(
        label="",
        max_length=100,
        widget=forms.TextInput(
            attrs={"class": "form-control", "placeholder": "First Name"}
        ),
    )
    last_name = forms.CharField(
        label="",
        max_length=100,
        widget=forms.TextInput(
            attrs={"class": "form-control", "placeholder": "Last Name"}
        ),
    )
    USER_TYPES = [
        ("arrendador", "Arrendador"),
        ("vendedor", "Vendedor"),
        ("usuario_normal", "Usuario Normal"),
    ]
    user_type = forms.ChoiceField(
        choices=USER_TYPES, widget=forms.RadioSelect, label="Tipo de Usuario"
    )

    class Meta:
        model = User  # Define el modelo asociado con este formulario
        fields = (
            "username",
            "first_name",
            "last_name",
            "email",
            "password1",
            "password2",
        )  # Define los campos que se incluirán en el formulario

    def __init__(self, *args, **kwargs):
        super(SignUpForm, self).__init__(*args, **kwargs)
        # Personaliza los atributos de los campos del formulario
        self.fields["username"].widget.attrs["class"] = "form-control"
        self.fields["username"].widget.attrs["placeholder"] = "User Name"
        self.fields["username"].label = ""
        self.fields["username"].help_text = (
            '<span class="form-text text-muted"><small>Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.</small></span>'
        )

        self.fields["password1"].widget.attrs["class"] = "form-control"
        self.fields["password1"].widget.attrs["placeholder"] = "Password"
        self.fields["password1"].label = ""
        self.fields["password1"].help_text = (
            "<ul class=\"form-text text-muted small\"><li>Your password can't be too similar to your other personal information.</li><li>Your password must contain at least 8 characters.</li><li>Your password can't be a commonly used password.</li><li>Your password can't be entirely numeric.</li></ul>"
        )

        self.fields["password2"].widget.attrs["class"] = "form-control"
        self.fields["password2"].widget.attrs["placeholder"] = "Confirm Password"
        self.fields["password2"].label = ""
        self.fields["password2"].help_text = (
            '<span class="form-text text-muted"><small>Enter the same password as before, for verification.</small></span>'
        )





class InmuebleSearchForm(forms.Form):
    region = forms.ModelChoiceField(queryset=Region.objects.all(), required=False, label="Región")
    comuna = forms.ModelChoiceField(queryset=Comuna.objects.all(), required=False, label="Comuna")
    dormitorios = forms.ChoiceField(choices=[(i, i) for i in range(1, 6)], required=False, label="Dormitorios")
    baños = forms.ChoiceField(choices=[(i, i) for i in range(1, 6)], required=False, label="Baños")
    tipo_inmueble = forms.ChoiceField(choices=[("Residencial", "Residencial"), ("Comercial", "Comercial")], required=False, label="Tipo")
    estado = forms.ChoiceField(choices=[("En Venta", "En Venta"), ("En Alquiler", "En Alquiler")], required=False, label="Estado de la propiedad")
    precio_min = forms.DecimalField(max_digits=10, decimal_places=2, required=False, label="Precio Mínimo uf")
#    precio_max = forms.DecimalField(max_digits=10, decimal_places=2, required=False, label="Precio Máximo")
    fecha_inicio = forms.DateField(widget=forms.SelectDateWidget, required=False, label="Fecha de Inicio")
    fecha_fin = forms.DateField(widget=forms.SelectDateWidget, required=False, label="Fecha de Fin")
