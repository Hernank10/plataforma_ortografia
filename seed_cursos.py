import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
django.setup()

from django.contrib.auth.models import User
from ejercicios.models import Curso, Ejercicio

def crear_datos():
    profe = User.objects.filter(is_superuser=True).first()
    if not profe:
        print("❌ Error: Crea un superusuario primero con 'python manage.py createsuperuser'")
        return

    cursos_data = [
        {"nombre": "Desafío de Tildes", "desc": "Reglas de acentuación: agudas, graves y esdrújulas."},
        {"nombre": "Duelo de la B y la V", "desc": "Uso de prefijos y homófonos confusos."},
        {"nombre": "Signos que Dan Vida", "desc": "Puntuación avanzada y uso de la coma."},
        {"nombre": "G, J y H: Las Invisibles", "desc": "Ortografía de verbos y palabras de origen árabe."},
        {"nombre": "Ortografía para Negocios", "desc": "Redacción formal y vicios del lenguaje."},
    ]

    for c in cursos_data:
        curso, created = Curso.objects.get_or_create(
            nombre=c['nombre'],
            defaults={'descripcion': c['desc'], 'profesor': profe}
        )
        if created:
            print(f"✅ Curso creado: {curso.nombre}")
            # Creamos un ejercicio base para cada uno
            Ejercicio.objects.create(
                curso=curso,
                palabra_correcta="Prueba",
                frase=f"Esto es un ejercicio inicial de {curso.nombre}.",
                nivel=1,
                creado_por=profe
            )

    print("\n🚀 ¡Base de datos poblada con éxito!")

if __name__ == '__main__':
    crear_datos()

