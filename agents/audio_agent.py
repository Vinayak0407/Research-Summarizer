import os
import pyttsx3

try:
    from elevenlabs import generate, play, save, set_api_key
    elevenlabs_available = True
except ImportError:
    elevenlabs_available = False

# Set your ElevenLabs API key from the environment
ELEVEN_API_KEY = os.getenv("ELEVEN_API_KEY")
if ELEVEN_API_KEY and elevenlabs_available:
    set_api_key(ELEVEN_API_KEY)

def generate_audio(text, filename="output_audio.mp3", voice="Rachel"):
    if ELEVEN_API_KEY and elevenlabs_available:
        print("[audio_agent] 🎤 Using ElevenLabs to generate audio...")
        audio = generate(text=text, voice=voice, model="eleven_monolingual_v1")
        save(audio, filename)
        print(f"[audio_agent] ✅ Audio saved as {filename}")
    else:
        print("[audio_agent] 🎤 Using offline TTS engine (pyttsx3)...")
        engine = pyttsx3.init()
        engine.save_to_file(text, filename)
        engine.runAndWait()
        print(f"[audio_agent] ✅ Offline audio saved as {filename}")
