import whisper
from resemblyzer import VoiceEncoder, preprocess_wav

model = whisper.load_model("base")
encoder = VoiceEncoder()

def transcribe_audio(file_path):
    result = model.transcribe(file_path)
    return result['text']

def get_voice_embedding(file_path):
    wav = preprocess_wav(file_path)
    embedding = encoder.embed_utterance(wav)
    return embedding.tolist()