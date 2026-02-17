from django.db import models
from django.utils.translation import gettext_lazy as _

class Ejercicio(models.Model):
    palabra_correcta = models.CharField(_("Palabra Correcta"), max_length=100)
    frase = models.TextField(_("Frase con hueco"))
    nivel = models.IntegerField(_("Nivel"), default=1)
    activo = models.BooleanField(default=True) # <-- Añadimos este para el .filter(activo=True)

    def __str__(self):
        return self.palabra_correcta
