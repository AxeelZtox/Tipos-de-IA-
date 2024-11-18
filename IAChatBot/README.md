# Asistente Virtual - Documentación

## Descripción General
Este proyecto consiste en un Asistente Virtual escrito en Python que utiliza la biblioteca NLTK (Natural Language Toolkit) para procesar lenguaje natural. El asistente es capaz de:

- Responder a saludos y preguntas comunes.
- Proporcionar información meteorológica de una ciudad específica.
- Realizar cálculos matemáticos simples.
- Finalizar la conversación al detectar palabras de despedida.

## Características
- **Interacción en Lenguaje Natural:** Utiliza patrones de expresiones regulares para entender y responder al usuario.
- **Información Meteorológica:** Se integra con la API de OpenWeatherMap para obtener datos del clima en tiempo real.
- **Cálculos Matemáticos:** Evalúa expresiones matemáticas de forma segura sin utilizar `eval`.
- **Personalizable:** La lista de patrones y respuestas (`pairs`) se puede ampliar para agregar más funcionalidades.

## Requisitos del Sistema
- **Python 3.6 o superior.**
- **Bibliotecas de Python:**
  - `nltk`
  - `requests`
- **Conexión a Internet** (para obtener información meteorológica).

## Instalación
### 1. Clonar el Repositorio o Descargar los Archivos
Descarga el archivo `asistente_virtual.py` y guárdalo en un directorio de tu elección.

### 2. Instalar Python 3.6 o Superior
Si aún no tienes Python instalado, puedes descargarlo desde [python.org](https://www.python.org/).

### 3. Crear un Entorno Virtual (Opcional pero Recomendado)
Es buena práctica crear un entorno virtual para gestionar las dependencias del proyecto.

```bash
python -m venv mi_entorno
