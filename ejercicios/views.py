import random
from django.shortcuts import render
from .models import EjercicioOrtografia

def juego_ortografia(request):
    # Intentamos obtener un ejercicio al azar que esté activo
    ejercicios = EjercicioOrtografia.objects.filter(activo=True)
    
    if not ejercicios:
        return render(request, 'ejercicios/juego.html', {'error': 'No hay ejercicios cargados todavía.'})

    # Seleccionamos uno al azar
    ejercicio = random.choice(ejercicios)
    
    # Preparamos el contexto para la plantilla
    context = {
        'ejercicio': ejercicio,
        'frase_mostrar': ejercicio.frase_incompleta.replace(ejercicio.palabra_correcta, "_______")
    }
    
    # Si el usuario envió una respuesta
    if request.method == 'POST':
        respuesta_usuario = request.POST.get('respuesta', '').strip().lower()
        correcta = ejercicio.palabra_correcta.lower()
        
        if respuesta_usuario == correcta:
            context['resultado'] = '¡Excelente! Has acertado.'
            context['clase_css'] = 'success'
        else:
            context['resultado'] = f'Casi... la palabra correcta es "{ejercicio.palabra_correcta}".'
            context['clase_css'] = 'danger'

    return render(request, 'ejercicios/juego.html', context)
