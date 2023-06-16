from django.db import models

# Create your models here.
class Acerca(models.Model):
    title = models.CharField(max_length=200, 
        verbose_name="Título")
    content = models.TextField(
        verbose_name="Contenido")
    image = models.ImageField(verbose_name="Imagen", 
        upload_to="Skill")
    created = models.DateTimeField(auto_now_add=True, 
        verbose_name="Fecha de creación")
    updated = models.DateTimeField(auto_now=True, 
        verbose_name="Fecha de edición")

    class Meta:
        verbose_name = "acerca"
        ordering = ['-created']

    def __str__(self):
        return self.title