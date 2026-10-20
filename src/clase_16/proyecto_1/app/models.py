from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Curso(models.Model):
    nombre=models.CharField(max_length=40)
    camada= models.IntegerField()
    def __str__(self) -> str:
        return f"{self.nombre} - {self.camada}"

class Estudiante(models.Model):
    nombre=models.CharField(max_length=40)
    apellido=models.CharField(max_length=40)  #una vez cambiamos el model, debemos actualizar la base de datos (faltan migraciones)
    email = models.EmailField()
    def __str__(self) -> str:
        return f"{self.nombre} - {self.apellido} | {self.email}" #recodar que desde aquí comienza el dato que ingresara a los forms

class Profesor(models.Model):
    nombre=models.CharField(max_length=40)
    apellido=models.CharField(max_length=40)
    email=models.EmailField()
    profesion=models.CharField(max_length=40)
    def __str__(self) -> str:
        return f"{self.nombre} - {self.apellido} | {self.profesion}"
class Entregable(models.Model):
    nombre=models.CharField(max_length=40)
    fecha_entrega=models.DateField(max_length=40)
    entregado=models.BooleanField(default=False)
    def __str__(self) -> str: #fixeamos el bug cursos object 1
        return f"{self.nombre} - {self.fecha_entrega} | {self.entregado}"

class Avatar(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='avatar')
    imagen = models.ImageField(upload_to='avatares', null=True, blank=True)
    def __str__(self):
        return f'Avatar de {self.user.username}'