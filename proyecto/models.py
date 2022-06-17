from django.db import models


class familiar (models.Model):
    Nombre= models.CharField ("Nombre" , max_length=30,)
    Nacimiento= models.DateField ("Nacimiento",)
    Edad= models.PositiveIntegerField("Edad",)
    Trabajo= models.CharField ("Trabajo", max_length=20,)