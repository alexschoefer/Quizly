import os
import whisper

"""
This module provides functionality to transcribe audio files using the Whisper model.
"""
model = whisper.load_model("base")

def transcribe_audio(file_path: str) -> str:
    """
    Transcribes the audio from the given file path using the Whisper model.
        Args:
            file_path (str): The path to the audio file to be transcribed.
        Returns:  
            str: The transcribed text from the audio file.
    """
    audio_path = os.path.abspath(file_path)
    result = model.transcribe(audio_path)
    return result["text"]