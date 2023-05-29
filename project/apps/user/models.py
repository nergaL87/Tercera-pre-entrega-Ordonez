from django.db import models

# Create your models here.
class User(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    nacimiento = models.DateField(null=True)

    def __str__(self):
        return f"{self.nombre} {self.apellido}"