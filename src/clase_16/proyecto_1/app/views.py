from django.shortcuts import render
from django.views import View
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from .forms import UserRegisterForm

from django.contrib.auth.mixins import LoginRequiredMixin

import os
from django.shortcuts import redirect
from django.urls import reverse_lazy

from django.views.generic.edit import CreateView
from .models import Avatar
from .forms import AvatarModelForm


from .models import Curso,Estudiante
from .forms import CursoModelForm, EstudianteModelForm


class CursoCreateView(CreateView):
    model = Curso # Modelo objetivo
    form_class = CursoModelForm # El formulario inteligente asociado
    template_name = 'curso_form.html' # HTML a renderizar
    success_url = reverse_lazy('lista_cursos') # Redirección perezosa tras éxito
# Nota técnica: CreateView procesa los métodos GET, POST, la validación
# interna de datos y la invocación de .save() de manera automática.



# Create your views here.
class InicioView(LoginRequiredMixin, View):
    def get(self, request):
        contexto=dict( #podemos pasarle variables a un html
            mensaje="Este es el inicio de tu App de Django", titulo="Home"

        )
        return render(request, "index.html", contexto)
                    #le pasamos el objeto request que espera un html
                                                     # la var es un diccionario

# LIST
class EstudianteListView(LoginRequiredMixin,ListView):
    model = Estudiante
    template_name = 'lista_estudiantes.html'
    context_object_name = 'estudiantes'

# CREATE
class EstudianteCreateView(LoginRequiredMixin ,CreateView):
    model = Estudiante
    form_class = EstudianteModelForm
    template_name = 'estudiantes.html'
    success_url = reverse_lazy('estudiantes')
    # --- UPDATE (Editar)
class EstudianteUpdateView(LoginRequiredMixin ,UpdateView):
    model = Estudiante
    form_class = EstudianteModelForm
    template_name = 'estudiantes.html'  # Reutiliza el formulario inteligente
    success_url = reverse_lazy('estudiantes')

# --- DELETE (Borrar)
class EstudianteDeleteView(LoginRequiredMixin ,DeleteView):
    model = Estudiante
    template_name = 'estudiante_confirm_delete.html'  # Template de confirmación de borrado
    success_url = reverse_lazy('estudiantes')
class CursoView(LoginRequiredMixin ,View):
    def get(self, request):
        contexto = dict(  # podemos pasarle variables a un html
            mensaje="Vista de Cursos", titulo="Cursos", cursos=Curso.objects.all()#le pasamos (*)toda la tabla
        )
        return render(request,"lista_cursos.html", contexto)


class ProfesoresView(LoginRequiredMixin ,View):
    def get(self, request):
        contexto = dict(  # podemos pasarle variables a un html
            mensaje="Vista de Profesores", titulo="Profesores"
        )
        return render(request, "index.html", contexto)


    class Meta:
        verbose_name = "Profesor"
        verbose_name_plural = "Profesores"
class EstudiantesView(LoginRequiredMixin ,View):
    def get(self, request):
        contexto = dict(  # podemos pasarle variables a un html
            mensaje="Vista de Estudiantes", titulo="Estudiantes"
        )
        return render(request,"index.html", contexto)
    #def __str__(self) -> str:
    #    return f"{self.nombre} - {self.apellido} | {self.email}"

class EntregablesView(LoginRequiredMixin ,View):
    def get(self, request):
        contexto = dict(  # podemos pasarle variables a un html
            mensaje="Vista de Entregables", titulo="Entregables"
        )
        return render(request,"index.html", contexto)

class RegistroView(LoginRequiredMixin,CreateView):
    form_class = UserRegisterForm
    template_name = 'registro.html'
    success_url = reverse_lazy('login')  # Redirección al loginpost-registro

# -------------- AVATAR ------------------
class AgregarAvatarView(LoginRequiredMixin, CreateView):
    model = Avatar
    form_class = AvatarModelForm
    template_name = 'agregar_avatar.html'
    success_url = reverse_lazy('home')


def form_valid(self, form):
    avatar_viejo = Avatar.objects.filter(user=self.request.user).first()


    if avatar_viejo:
        if avatar_viejo.imagen and os.path.isfile(
                avatar_viejo.imagen.path
        ):
            os.remove(avatar_viejo.imagen.path)
        avatar_viejo.delete()

    avatar = form.save(commit=False)
    avatar.user = self.request.user
    avatar.save()
    return redirect(self.success_url)