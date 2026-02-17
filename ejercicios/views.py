import random
from django.shortcuts import render, get_object_or_404
from .models import Ejercicio, Curso

def inicio(request):
    """Página de bienvenida y acceso a la lista de cursos"""
    return render(request, 'ejercicios/inicio.html')

def lista_cursos(request):
    """Muestra los 5 cursos que creamos con el seed"""
    cursos = Curso.objects.all()
    return render(request, 'ejercicios/lista_cursos.html', {'cursos': cursos})

def juego_ortografia(request, curso_id):
    """Vista del juego filtrada por un curso específico"""
    curso = get_object_or_404(Curso, pk=curso_id)
    ejercicios = Ejercicio.objects.filter(curso=curso, activo=True)
    
    if not ejercicios.exists():
        return render(request, 'ejercicios/juego.html', {
            'error': 'Este curso aún no tiene ejercicios.',
            'curso': curso
        })
    
    # Seleccionamos un ejercicio al azar del curso elegido
    ejercicio = random.choice(ejercicios)
    
    context = {
        'ejercicio': ejercicio,
        'curso': curso,
        'frase_mostrar': ejercicio.frase.replace(ejercicio.palabra_correcta, "_______")
    }
    
    if request.method == 'POST':
        respuesta_usuario = request.POST.get('respuesta', '').strip().lower()
        correcta = ejercicio.palabra_correcta.lower()
        
        if respuesta_usuario == correcta:
            context['resultado'] = '¡Excelente! Has acertado.'
            context['clase_css'] = 'success'
        else:
            context['resultado'] = f'Casi... la respuesta era: {ejercicio.palabra_correcta}'
            context['clase_css'] = 'danger'
            
    return render(request, 'ejercicios/juego.html', context)
