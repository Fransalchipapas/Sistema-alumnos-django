from django import forms
from .models import Curso, Estudiante
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Avatar

class CursoModelForm(forms.ModelForm):
    class Meta:
        model = Curso # Vinculación explícita con el modelo físico
        fields = ['nombre', 'camada'] # Columnas expuestas en la interfaz
        # Sobreescritura visual y adición de clases de diseño (Bootstrap)
        labels = {
            'nombre': 'Nombre del Curso',
            'camada': 'Número de Camada'
        }
        widgets = {
        'nombre': forms.TextInput(attrs={'placeholder': 'Ej:Python'}),
        'camada': forms.NumberInput(attrs={'placeholder': 'Ej:12121212'}),
        }

class EstudianteModelForm(forms.ModelForm):

    class Meta:
        model = Estudiante  # Vinculación explícita con el modelo físico

        fields = ['nombre', 'apellido', 'email']

        # Etiquetas personalizadas
        labels = {
            'nombre': 'Nombre',
            'apellido': 'Apellido',
            'email': 'Correo Electrónico',
        }

        # Widgets y atributos HTML
        widgets = {
            'nombre': forms.TextInput(
                attrs={'placeholder': 'Ej: Juan'}
            ),
            'apellido': forms.TextInput(
                attrs={'placeholder': 'Ej: Pérez'}
            ),
            'email': forms.EmailInput(
                attrs={'placeholder': 'Ej: juan@email.com'}
            ),
        }
class UserRegisterForm(UserCreationForm):
    email = forms.EmailField(label="Correo Electrónico", required=True)
    password1 = forms.CharField(label="Contraseña",
    widget=forms.PasswordInput)
    password2 = forms.CharField(label="Repetir contraseña",
    widget=forms.PasswordInput)
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
class AvatarModelForm(forms.ModelForm):
    class Meta:
        model = Avatar
        fields = ['imagen']
        labels = {'imagen': 'Selecciona tu foto de perfil'} #recordar que si makemigrations da error primero revisa aqui en forms los errores