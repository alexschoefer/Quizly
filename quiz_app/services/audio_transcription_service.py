import os
import whisper

def transcribe_audio(file_path: str) -> str:
    """
    Transcribes the audio from the given file path using the Whisper model.
        Args:
            file_path (str): The path to the audio file to be transcribed.
        Returns:  
            str: The transcribed text from the audio file.
    """
    model = whisper.load_model("base")
    audio_path = os.path.abspath(file_path)
    result = model.transcribe(audio_path)
    return result["text"]