import streamlit as st
import requests
import tempfile
import os
import sounddevice as sd
import wave

# Streamlit app title
st.title("🌟 Sunbird ALL - Assisted Language Learning")

# Language selection dropdown
language = st.selectbox("🌐 Select Language:", ["English", "Hindi", "Spanish"], index=0)
st.write(f"Selected Language: {language}")

# Feedback section
feedback_placeholder = st.empty()

# Audio recording functionality
def record_audio(duration=5, samplerate=16000):
    """Record audio for a fixed duration."""
    st.write("🎙️ Recording... Please speak now.")
    audio_data = sd.rec(int(duration * samplerate), samplerate=samplerate, channels=1, dtype='int16')
    sd.wait()  # Wait until recording is finished
    st.write("✅ Recording complete.")
    return audio_data

# Button to start/stop recording
if st.button("🎤 Start Speaking"):
    duration = st.slider("⏱️ Recording Duration (seconds):", min_value=1, max_value=10, value=5)
    try:
        audio_data = record_audio(duration=duration)

        # Save audio to a temporary file
        with tempfile.NamedTemporaryFile(delete=False, suffix=".wav") as temp_audio_file:
            temp_file_name = temp_audio_file.name
            with wave.open(temp_file_name, 'w') as wf:
                wf.setnchannels(1)
                wf.setsampwidth(2)
                wf.setframerate(16000)
                wf.writeframes(audio_data.tobytes())

        # Send audio to backend
        feedback_placeholder.text("⏳ Processing your audio...")
        try:
            with open(temp_file_name, "rb") as audio_file:
                response = requests.post("http://127.0.0.1:8000/asr", files={"file": audio_file})
                if response.status_code == 200:
                    result = response.json()
                    feedback_placeholder.text(f"📝 Transcription: {result.get('text', 'No text detected.')}")
                else:
                    feedback_placeholder.text(f"❌ Error: {response.status_code} - {response.text}")
        except requests.exceptions.RequestException as e:
            feedback_placeholder.text(f"❌ Network Error: {e}")
        finally:
            # Ensure the temporary file is deleted after processing
            if os.path.exists(temp_file_name):
                os.unlink(temp_file_name)
    except Exception as e:
        feedback_placeholder.text(f"❌ Recording Error: {e}")

# Dashboard section
st.subheader("📊 Dashboard")
st.write("Progress and insights will be displayed here...")