## Vistas basadas en clases
Se usa en tareas repetitivas (mostrar listas, formularios de creacion/edicion)
Reducen costo repetitivo y mejoran la organización mediante herencia
deventaja=volverse difícil de leer y personalizar si la logica rompe la estructura
## Vistas basadas en funciones 
Se usa con procesos unicos, APIs simples o lógica que requiere un control exacto paso a paso 
Facil de leer y escribir. Flujo explícito desde el primer vistazo
Deventaja= Tienden a duplicar el código)(boilerplate) cuando se manejan operaciones CRUD consecutivas

---
CBV para código DRY en lo estándar, y FBV para mantenerlo claro en lo complejo
 ## MODELO
EL modelo es la parte de nuestro proyecto que alamcena borra, modifica y manipula el caudal principal de los datos apoyándose en alguna db
Para django un proyecto es un conjunto de aplicaciones c/u con funcion propia}

## Comandos que lanzamos en orden
```text
uv init #en la carpeta de trabajo
uv add django --> despues activamos el entorno
vamos adentro de crs, luego al proyecto -->django-admin  startproject "Proyecto1"
django-admin  startproject "Proyecto1 . -->  el punto al final indica que la creacion a hace adentro de esa misma carpeta sin crear otra
python manage.py startapp app -->creamos la app con su estructura + migration 

```
Las aplicaciones tienen la carpeta migrations, aquá se un guarda registro, al ejecutar migrate lo pasa a la DB 

## CREAMOS EL MODELO DESPUÉS INFORMAMOS A DJANGO
## Comandos que lanzamos en orden
```text
python manage.py check -> comando para verificar integridad (antes vamos a settings en proyecto INSTALLED APPS= ['app',]) 
vamos a la carpeta que tiene el manage -> python manage.py migrate (creamos la base de datos)
python manage.py runserver   (levantamos el servidor)
creamos el modulo de las vistas en el directorio que contiene la config de los modulos

```
<h2> Creamos el modelo BB.DD </h2>

```text
python manage.py makemigrations  -> nos genera el 001, generamos la estructura de la DB
python manage.py migrate -> construimos la DB
vamos a la carpeta que tiene el manage -> python manage.py migrate (creamos la base de datos)


```
##CREAMOS VISTAS
creamos la carpeta templates con su index.html
codeamos todas las vistas 
vamos a apps.py
## CREAMOS LAS URLS
Le tenemos que indicar al \proyecto_1 que mira a las urls de \app
Copiamos de \proyecto_1\urls
codeamos las urls en \app\
## Asociamos los recursos
Incluimos las urls a \proyecto_1\urls
## Probamos la aplicación
```text
python manage.py runserver   (levantamos el servidor)

creamos el modulo de las vistas en el directorio que contiene la config de los modulos

```
Entramos a http://127.0.0.1:8000/app/
Accedemos a las vistas http://127.0.0.1:8000/app/curso/
                        http://127.0.0.1:8000/app/profesores/ 
                        ...
##  editamos models.py
```text
python manage.py makemigrations  #debido a que se realizaron cambios que afectaron la DB
python manage.py migrate
```
## En la clase 8 también nos encontraremos con las vistas basadas en .. que pueden sumarse al proyecto final
en Guia_Implementacion_Avatar nos encontramos con : : Renderizado en el Navbar o interfaz (base.html que debe aplicarse tambien
## MIDELWERE
Es una función o clase que media en una petición, debido a que intercepta los datos mientras viajan hacia la vista 

## Desplegar en REDER | django_environ_render.pdf
instalamos uv add gunicorn / psycopg2-binary / dj-database-url / whitenoise / django-environ 
Creamos el archivo .env en raiz y le pasamos 
```text
DEBUG=True
SECRET_KEY=django-insecure-cambiar-esto-en-produccion-123456
DATABASE_URL=postgres://usuario:password@localhost:5432/tienda_lacteos
```
Actualizamos el .gitignore con .env + db.sqlite3
Después adaptamos el archivo settings.py y configurar también DATABASES  | pasos_despliegue_render.pdf
## Pegamos el Dokerfile 
Pegamos el archivo a la altura de manage.py

```text
    git init
    git commit -m "primer commit"
    
```
