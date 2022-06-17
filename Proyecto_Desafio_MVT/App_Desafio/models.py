from django.db import models

# Create your models here.
class Familia(models.Model):
    edad = models.IntegerField()
    parentezco = models.CharField(max_length=15)
    fecha_cumpleanios = models.DateField()
