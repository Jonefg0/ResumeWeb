from django.db import models

# Create your models here.

class Project(models.Model):
    title = models.CharField(max_length=255, verbose_name="Titulo")
    description = models.TextField(verbose_name="Descripción")
    image = models.ImageField(verbose_name="Imagen", upload_to="projects")
    created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha creación")
    updated = models.DateTimeField(auto_now=True, verbose_name="Última actualización")
    URLField = models.URLField(verbose_name="URL", blank= True, null=True)

    class Meta:
        verbose_name = "proyecto"
        verbose_name_plural = "proyectos"
        ordering = ["-created"] # el "-"  indica que es desde el más nuevo al más antiguo
    
    def __str__(self):
        return self.title