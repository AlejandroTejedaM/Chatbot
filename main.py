import time

from fastapi import FastAPI
from pydantic import BaseModel
from starlette.middleware.cors import CORSMiddleware
from KnowledgeGraph import responder_pregunta
import sys
import queue
import sounddevice as sd
import json
from vosk import Model, KaldiRecognizer
from pydub import AudioSegment
AudioSegment.converter = r"C:\ffmpeg\bin\ffmpeg.exe"
AudioSegment.ffmpeg = r"C:\ffmpeg\bin\ffmpeg.exe"
AudioSegment.ffprobe = r"C:\ffmpeg\bin\ffprobe.exe"

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # You can specify a list of allowed origins instead of ["*"]
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Inicializar modelo de Vosk
model_path = "C:/Users/alex2/PycharmProjects/vosk/vosk-model-es-0.42"
try:
    model = Model(model_path)
    print("Modelo de Vosk cargado correctamente.")
except Exception as e:
    print(f"Error cargando el modelo de Vosk: {e}")
    sys.exit(1)

# Configurar reconocimiento de voz
rec = KaldiRecognizer(model, 16000)
rec.SetWords(True)
audio_queue = queue.Queue()


# Callback para capturar audio
def callback(indata, frames, time, status):
    if status:
        print(status, file=sys.stderr)
    audio_queue.put(bytes(indata))

class Question(BaseModel):
    pregunta: str

@app.post("/preguntar")
def preguntar(question: Question):
    respuesta = responder_pregunta(question.pregunta)
    return {"respuesta": respuesta}
@app.get("/")
def read_root():
    return {"Hello": "World"}


# In main.py, modify the /voz/ endpoint
@app.get("/voz/")
async def consulta_voz():
    try:
        timeout = 5  # 5 seconds timeout
        data_collected = []

        with sd.RawInputStream(samplerate=16000, blocksize=8000, dtype="int16",
                               channels=1, callback=callback):
            print("Escuchando...")
            start_time = time.time()

            while True:
                try:
                    # Get data with timeout
                    data = audio_queue.get(timeout=0.5)
                    data_collected.append(data)

                    if rec.AcceptWaveform(data):
                        resultado = json.loads(rec.Result())["text"]
                        if resultado.strip():  # If we got text
                            print(f"Texto reconocido: {resultado}")
                            respuesta = responder_pregunta(resultado)
                            return {"pregunta": resultado, "respuesta": respuesta, "status": "success"}

                    # Check timeout
                    if time.time() - start_time > timeout:
                        return {"status": "timeout", "error": "Tiempo de espera agotado"}

                except queue.Empty:
                    continue

    except Exception as e:
        print(f"Error: {e}")
        return {"status": "error", "error": str(e)}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)