from mutagen.mp3 import MP3
from mutagen.oggvorbis import OggVorbis
from mutagen.flac import FLAC
from mutagen.wave import WAVE
import os

def get_audio_length(file_path):
    ext = os.path.splitext(file_path)[1].lower()  # Get the file extension
    if ext == ".mp3":
        audio = MP3(file_path)
    elif ext == ".ogg":
        audio = OggVorbis(file_path)
    elif ext == ".flac":
        audio = FLAC(file_path)
    elif ext == ".wav":
        audio = WAVE(file_path)
    else:
        raise ValueError(f"Unsupported file format: {ext}")

    return audio.info.length