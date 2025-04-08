from django.db import models

# Create your models here.
class Familiares(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    edad = models.IntegerField()
    fecha_nacimiento = models.DateTimeField()

    def __str__(self):
        return f"{self.nombre} {self.apellido} de {self.edad} años de edad, nacido el {self.fecha_nacimiento}"