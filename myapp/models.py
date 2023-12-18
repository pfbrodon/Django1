from django.db import models

# Create your models here.
class Proyecto(models.Model):
    nombre=models.CharField(max_length=200)
    
class Tareas(models.Model):
    titulo=models.CharField(max_length=100)
    descripcion=models.TextField()
    proyecto=models.ForeignKey(Proyecto, on_delete=models.CASCADE)