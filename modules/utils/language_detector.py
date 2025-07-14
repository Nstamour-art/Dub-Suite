import os
from typing import Optional
from faster_whisper import WhisperModel
import torch
from audio_utils import AudioUtils


class LanguageDetector:
    def __init__(self, model_size="tiny", device="auto") -> None:
        """Initializes the LanguageDetector with a specific model size and device.

        Args:
            model_size (str, optional): The size of the model to use. Defaults to "tiny".
            device (str, optional): The device to run the model on. Defaults to "auto".
        """
        if device == "auto":
            device = "cuda" if torch.cuda.is_available() else "cpu"

        compute_type = "float16" if device == "cuda" else "int8"
        try:
            self.model = WhisperModel(
                model_size, device=device, compute_type=compute_type
            )
        except Exception as e:
            raise RuntimeError(f"Failed to initialize model: {e}")

    def detect_language(self, audio_path) -> Optional[str]:
        """Detects the language of the audio file.
        This method checks the audio file format and converts it to WAV if necessary.
        Args:
            audio_path (str): The path to the audio file.

        Returns:
            str: The detected language code.
        """
        if not audio_path.endswith((".mp3", ".wav", ".flac", ".m4a")):
            audio_path = AudioUtils.convert_audio_format(audio_path, "wav")
        elif not os.path.isfile(audio_path):
            raise ValueError("Audio file does not exist.")
        try:
            _, info = self.model.transcribe(audio_path, beam_size=1)
            return info.language
        except Exception as e:
            raise RuntimeError(f"Failed to detect language: {e}")
