from django.urls import path
from . import views

urlpatterns = [
    # Página de inicio (Bienvenida)
    path('', views.inicio, name='inicio'),
    
    # Lista de los 5 cursos disponibles
    path('cursos/', views.lista_cursos, name='lista_cursos'),
    
    # El juego filtrado por el ID del curso
    # Ejemplo: /juego/1/
    path('juego/<int:curso_id>/', views.juego_ortografia, name='juego_ortografia'),
]
