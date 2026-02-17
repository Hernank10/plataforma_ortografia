import os
import re
from deep_translator import GoogleTranslator

def traducir_archivo_po(ruta_archivo, lang_destino):
    print(f"--- Traduciendo {lang_destino} en {ruta_archivo} ---")
    
    # Mapeo de códigos de Django a códigos de Google Translator
    mapeo_idiomas = {
        'zh_hans': 'zh-CN',
        'ar': 'ar',
        'en': 'en',
        'fr': 'fr',
    }
    
    target_lang = mapeo_idiomas.get(lang_destino.lower(), lang_destino.lower())
    translator = GoogleTranslator(source='es', target=target_lang)

    with open(ruta_archivo, 'r', encoding='utf-8') as f:
        lineas = f.readlines()

    nuevas_lineas = []
    msgid_actual = ""
    
    for linea in lineas:
        if linea.startswith('msgid "'):
            # Extraer el texto entre comillas
            match = re.search(r'msgid "(.*)"', linea)
            if match:
                msgid_actual = match.group(1)
        
        if linea.startswith('msgstr ""') and msgid_actual:
            try:
                # Solo traducimos si el msgid no está vacío
                traduccion = translator.translate(msgid_actual)
                linea = f'msgstr "{traduccion}"\n'
                print(f"  OK: {msgid_actual} -> {traduccion}")
            except Exception as e:
                print(f"  Error en '{msgid_actual}': {e}")
            msgid_actual = "" # Resetear para el siguiente
        
        nuevas_lineas.append(linea)

    with open(ruta_archivo, 'w', encoding='utf-8') as f:
        f.writelines(nuevas_lineas)

# Escanear la carpeta locale
ruta_locale = './locale'
if os.path.exists(ruta_locale):
    for lang in os.listdir(ruta_locale):
        ruta_po = os.path.join(ruta_locale, lang, 'LC_MESSAGES', 'django.po')
        if os.path.exists(ruta_po):
            traducir_archivo_po(ruta_po, lang)

print("\n✅ ¡Traducción automática finalizada con deep-translator!")
