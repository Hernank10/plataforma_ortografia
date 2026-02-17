from django.contrib import admin
from .models import Ejercicio

@admin.register(Ejercicio)
class EjercicioAdmin(admin.ModelAdmin):
    # Columnas que verá el profesor en la lista
    list_display = ('palabra_correcta', 'nivel', 'activo', 'creado_por')
    # Filtros laterales para facilitar el trabajo
    list_filter = ('nivel', 'activo')
    # Buscador de palabras
    search_fields = ('palabra_correcta', 'frase')

    def save_model(self, request, obj, form, change):
        # Asignamos automáticamente el profesor que creó el ejercicio
        if not obj.pk:
            obj.creado_por = request.user
        super().save_model(request, obj, form, change)

    def get_queryset(self, request):
        # Si es superusuario, ve todo. Si es profesor, solo ve sus ejercicios.
        qs = super().get_queryset(request)
        if request.user.is_superuser:
            return qs
        return qs.filter(creado_por=request.user)
