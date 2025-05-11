from fastapi import FastAPI, File, UploadFile
from vosk import Model, KaldiRecognizer
import wave
import json
import os

app = FastAPI()

# Update the model path to point to the specific model folder
model_path = os.path.join(os.path.dirname(__file__), "model", "vosk-model-small-en-us-0.15")
model = Model(model_path)

@app.get("/")
def read_root():
    return {"message": "Welcome to Sunbird ALL - Assisted Language Learning PoC"}

@app.post("/asr")
def speech_to_text(file: UploadFile = File(...)):
    try:
        # Save the uploaded file temporarily
        with open("temp.wav", "wb") as temp_file:
            temp_file.write(file.file.read())

        # Open the WAV file
        wf = wave.open("temp.wav", "rb")
        if wf.getnchannels() != 1 or wf.getsampwidth() != 2 or wf.getframerate() not in [8000, 16000]:
            return {"error": "Audio file must be WAV format mono PCM."}

        # Recognize speech using Vosk
        rec = KaldiRecognizer(model, wf.getframerate())
        result = ""
        while True:
            data = wf.readframes(4000)
            if len(data) == 0:
                break
            if rec.AcceptWaveform(data):
                result = json.loads(rec.Result())

        # Close the file
        wf.close()

        return {"text": result.get("text", "")}
    except Exception as e:
        return {"error": str(e)}