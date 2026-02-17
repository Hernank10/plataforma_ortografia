from django.db import models
from django.conf import settings
from django.utils.translation import gettext_lazy as _

class Curso(models.Model):
    nombre = models.CharField(_("Nombre del Curso"), max_length=200)
    descripcion = models.TextField(_("Descripción"))
    profesor = models.ForeignKey(
        settings.AUTH_USER_MODEL, 
        on_delete=models.CASCADE,
        related_name='cursos_dictados'
    )
    estudiantes = models.ManyToManyField(
        settings.AUTH_USER_MODEL, 
        related_name='cursos_inscritos', 
        blank=True
    )

    def __str__(self):
        return self.nombre

class Ejercicio(models.Model):
    # Relación con el curso
    curso = models.ForeignKey(
        Curso, 
        on_delete=models.CASCADE, 
        related_name='ejercicios', 
        null=True,
        blank=True
    )
    
    # Campos básicos del juego
    palabra_correcta = models.CharField(_("Palabra Correcta"), max_length=100)
    frase = models.TextField(_("Frase con hueco"))
    nivel = models.IntegerField(_("Nivel"), default=1)
    activo = models.BooleanField(default=True)
    
    # Campo para los Roles (Profesor que lo creó)
    creado_por = models.ForeignKey(
        settings.AUTH_USER_MODEL, 
        on_delete=models.SET_NULL, 
        null=True, 
        blank=True,
        verbose_name=_("Creado por")
    )

    def __str__(self):
        return f"{self.palabra_correcta} - {self.curso.nombre if self.curso else 'Sin Curso'}"
