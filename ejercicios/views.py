import random  # <--- ¡Faltaba esta! Sin ella, random.choice fallará.
from django.shortcuts import render
from .models import Ejercicio 

def inicio(request):
    """Vista para la página de bienvenida"""
    return render(request, 'ejercicios/inicio.html')

def juego_ortografia(request):
    """Vista principal del juego"""
    # Obtenemos todos los ejercicios
    ejercicios = Ejercicio.objects.all() 
    
    if not ejercicios.exists():
        return render(request, 'ejercicios/juego.html', {'error': 'No hay ejercicios en la base de datos.'})
    
    # Seleccionamos un ejercicio al azar
    ejercicio = random.choice(ejercicios)
    
    # Preparamos el contexto. 
    # Usamos .replace para ocultar la palabra correcta en la frase.
    context = {
        'ejercicio': ejercicio,
        'frase_mostrar': ejercicio.frase.replace(ejercicio.palabra_correcta, "_______")
    }
    
    # Lógica para procesar la respuesta del usuario
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
