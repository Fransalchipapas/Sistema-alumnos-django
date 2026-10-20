from django.urls import path
from .views import InicioView, CursoView, EstudiantesView, ProfesoresView, EntregablesView, CursoCreateView, EstudianteListView, EstudianteCreateView, EstudianteUpdateView, EstudianteDeleteView, AgregarAvatarView
            #importamos las vistas
from django.contrib.auth.views import LoginView, LogoutView
from .views import RegistroView
urlpatterns = [
    path('admin/', InicioView.as_view()),

    #vaciamos las rutas
                #seteamos como vista
    path('curso/', CursoView.as_view(),name='inicio'),
#    path('estudiantes/', EstudiantesView.as_view(), name='estudiantes'),# si django encuentra esta ruta nunca usara la del CRUD
    path('profesores/', ProfesoresView.as_view(),name='profesores'),
    path('entregables/', EntregablesView.as_view(), name='entregables'),

#    path('', HomeView.as_view(), name="home"),
#    path('cursos/', CursosView.as_view(), name='cursos'),
    path(
        'estudiantes/',
        EstudianteListView.as_view(),
        name='estudiantes'
    ),
    path(
        'estudiantes/crear/',
        EstudianteCreateView.as_view(),
        name='crear_estudiante'
    ),

    path(
        'estudiantes/editar/<int:pk>/',
        EstudianteUpdateView.as_view(),
        name='editar_estudiante'
    ),

    path(
        'estudiantes/eliminar/<int:pk>/',
        EstudianteDeleteView.as_view(),
        name='eliminar_estudiante'
    ),
    path('cursos/crear/', CursoCreateView.as_view(), name='crear_curso'),

    # RUTA DE LOGIN: Genera el formulario e inyecta la lógica automáticamente
    path(
    'login/',
    LoginView.as_view(template_name='login.html'),
    name='login'
    ),
    # RUTA DE LOGOUT: Procesa el cierre de sesión de forma segura
    path(
    'logout/',
    LogoutView.as_view(),
    name='logout'
    ),
    # RUTA DE REGISTRO: Para nuevos usuarios
    path(
    'registro/',
    RegistroView.as_view(),
    name='registro'
    ),

    #ENRATAMIENTO MODULA, agregamos las directicas de servicio multimedia
    path('agregar-avatar/',
    AgregarAvatarView.as_view(), #tambien verificar los errores en los path de las vistas
    name='agregar_avatar'
    )

]



