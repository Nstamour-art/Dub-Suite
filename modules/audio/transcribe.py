from faster_whisper import WhisperModel
import torch


class Transcriber:
    """Transcribes audio files using the Whisper model."""

    def __init__(self, model_size="large-v3", device="auto"):
        """Initializes the Transcriber with a specific model size and device.
        Args:
            model_size (str): The size of the Whisper model to use.
            device (str): The device to run the model on ("cpu" or "cuda").
        """
        if device == "auto":
            device = "cuda" if torch.cuda.is_available() else "cpu"
        compute_type = "float16" if device == "cuda" else "int8"
        self.model = WhisperModel(model_size, device=device, compute_type=compute_type)

    def transcribe(self, audio_file: str, language: str) -> dict:
        """
        Summary:
            Transcribes the given audio file into text and returns a dictionary
            with words and their timestamps in format "start - end": "word".
        Args:
            audio_file (str): The path to the audio file to transcribe.
            language (str): The language of the audio file.
        """
        transcript_with_word_timestamps = {}
        segments, _ = self.model.transcribe(
            audio_file,
            beam_size=5,
            word_timestamps=True,
            language=language,
            condition_on_previous_text=True,
            vad_filter=True,
            vad_parameters={
                "min_speech_duration_ms": 100,
                "min_silence_duration_ms": 100,
            },
            suppress_blank=True,
            temperature=0.01,
        )
        for segment in segments:
            for word in segment.words:
                transcript_with_word_timestamps[f"{word.start} - {word.end}"] = (
                    word.word
                )
        return transcript_with_word_timestamps
