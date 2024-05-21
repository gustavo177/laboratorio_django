from django.db import models

# Create your models here.
class Peliculas(models.Model):
    imagen = models.ImageField(upload_to='imagenes', null=True, blank=True)
    titulo = models.CharField(max_length=200)
    descripcion = models.TextField()
    precio = models.IntegerField()
    def __str__(self):
        return str(self.id) + " - " + self.titulo