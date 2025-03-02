# Sistema de Asistente Virtual para Enseñanza del Habla

## Descripción
Sistema interactivo que utiliza grafos de conocimiento y reconocimiento de voz para asistir en la enseñanza del habla. Integra una API REST con FastAPI y una interfaz web en React.

## Tecnologías Utilizadas
- Python 3.x
- FastAPIwww
- Vosk (Reconocimiento de voz)
- NetworkX (Grafos de conocimiento)
- React.js
- Node.js

## Requisitos Previos
- Python 3.x instalado
- Node.js y npm instalados
- FFmpeg instalado
- Modelo Vosk en español

## Instalación
### 1. Configuración del Entorno

1. Clonar el repositorio:
   ```bash
   git clone https://github.com/AlejandroTejedaM/Chatbot.git
   cd Chatbot
   ```
2. Instala las dependencias necesarias:
   ```bash
   pip install -r requirements.txt
   ```
3. Configurar FFmpeg:
    - Descarga FFmpeg en <https://ffmpeg.org/download.html>.
    - Agrega la carpeta bin de FFmpeg a las variables de entorno (Windows).
    - Verifica que FFmpeg esté correctamente instalado ejecutando el siguiente comando:
      ```bash
      ffmpeg -version
      ```
   - Confirmar rutas en el código:
      ````python
     AudioSegment.converter = r"C:\ffmpeg\bin\ffmpeg.exe"
     AudioSegment.ffmpeg = r"C:\ffmpeg\bin\ffmpeg.exe"
     AudioSegment.ffprobe = r"C:\ffmpeg\bin\ffprobe.exe"
      ````
4. Configurar Vosk:
   - Descarga el modelo `vosk-model-es-0.42` en <https://alphacephei.com/vosk/models>
   - Descomprimelo y asegúrate de colocar la ruta correcta en el archivo `main.py`:
     ````python
     model_path = "vosk-model-es-0.42"
     ````

### 2. Configuración del Frontend
1. Instala las dependencias de React:
   ```bash
   cd Web\client
   npm install
   ```
### 3. Ejecución
1. Ejecuta el servidor de FastAPI:
   ```bash
   uvicorn main:app --reload
   ```
2. Ejecuta el servidor de React:
   ```bash
   cd Web\client
   npm start
   ```
### 4. Uso
1. Abre tu navegador en `http://localhost:3000/` para acceder a la interfaz web.

## Tipos de Preguntas Soportadas

### 1. Preguntas sobre definiciones
- "¿Qué es el método global?"
- "¿Qué es el refuerzo positivo?"
- "¿Qué son las estrategias visuales?"

### 2. Preguntas sobre métodos
- "¿Cómo usar las estrategias visuales?"
- "¿Cómo aplicar el refuerzo positivo?"
- "¿Cómo qué cursos puedo trabajar?"
- "¿Cómo implementar el método fonológico?"

### 3. Preguntas sobre relaciones 
- "¿Qué está relacionado con las actividades prácticas?"
- "¿Qué es similar al método global?"
- "¿Qué se relaciona con los recursos educativos?"
- "¿Qué temas están relacionados con las estrategias de comunicación?"

### 4. Preguntas sobre recursos específicos
- "¿Qué actividades hay disponibles?"
- "¿Qué recursos educativos existen?"
- "¿Qué estrategias puedo usar?"
- "¿Qué ejercicios hay?"

### 5. Saludos
- "Hola"
- "Adiós"
