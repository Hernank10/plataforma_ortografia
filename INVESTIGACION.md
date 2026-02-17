# 📑 Proyecto de Investigación: Sistema Automatizado de Refuerzo Ortográfico Multilingüe (SAROM)

## 1. Introducción
Este documento detalla la investigación técnica y pedagógica detrás de la **plataforma_ortografia**. El proyecto busca resolver la brecha de accesibilidad en herramientas educativas digitales, permitiendo que el entrenamiento ortográfico sea accesible en más de 30 idiomas mediante la automatización de procesos.

## 2. Hipótesis de Investigación
"Es posible reducir drásticamente los tiempos de localización de software educativo mediante la integración de APIs de traducción neuronal dentro del flujo de trabajo de internacionalización (i18n) de Django, manteniendo una experiencia de usuario gamificada y coherente."

## 3. Pilares Tecnológicos

### A. Automatización de la Localización (i18n)
A diferencia de los métodos tradicionales donde cada cadena de texto se traduce manualmente, este proyecto investiga el uso de `deep-translator` para procesar archivos de catálogo de mensajes (`.po`).
- **Logro:** Reducción del tiempo de despliegue de un nuevo idioma de horas a segundos.
- **Desafío:** Validación de contextos semánticos en idiomas con gramáticas complejas (Árabe, Chino, Ruso).

### B. Arquitectura de Persistencia Efímera
Se estudia el uso de `Django Sessions` para el seguimiento del progreso (puntos y rachas) sin necesidad de bases de datos persistentes de usuario.
- **Ventaja:** Mayor privacidad y menor latencia.
- **Mecánica:** Implementación de contadores de racha ("Streaks") que fomentan la retención del usuario a través del refuerzo positivo.

### C. Diseño de Interfaz Adaptativa (RTL/LTR)
La investigación abarca la adaptación visual automática. La plataforma detecta si el idioma seleccionado es **RTL** (Right-to-Left) como el Árabe, ajustando el layout de Bootstrap para mantener la usabilidad.

## 4. Metodología Desarrollada
1. **Extracción:** Uso de `makemessages` para capturar cadenas de texto pedagógicas.
2. **Traducción Neuronal:** Procesamiento mediante el script personalizado `traducir_po.py`.
3. **Compilación:** Transformación a archivos binarios `.mo` para alta velocidad de lectura.
4. **Validación:** Ejecución de `python manage.py check` para asegurar la integridad del sistema.

## 5. Conclusiones Preliminares
- La automatización permite una **escalabilidad horizontal** sin precedentes en proyectos de código abierto.
- La gamificación básica (puntos/racha) aumenta el tiempo de permanencia en la aplicación en un entorno de pruebas controlado.

## 6. Trabajo Futuro
- Implementación de modo **"Speed Spell"** (análisis de tiempo de respuesta).
- Integración de síntesis de voz (Text-to-Speech) para dictados ortográficos multilingües.

---
**Investigador Principal:** Hernank10  
**Tecnologías:** Python 3.13, Django 5, Deep Learning Translation APIs.
