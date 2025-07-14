"""
Copyright © 2025 Nicolas St-Amour. All rights reserved.
Licensed under the Dub-Suite Source-Available License.

This software is source-available for educational and personal use only.
Commercial use requires explicit written permission.
"""

import os
from pydub import AudioSegment


class AudioUtils:

    @staticmethod
    def convert_audio_format(input_file: str, output_format: str) -> str:
        """Converts audio files to a specified format.

        Args:
            input_file (str): The path to the input audio file.
            output_format (str): The desired output audio format (e.g., "mp3", "wav").

        Returns:
            str: The path to the converted audio file.
        """
        if not os.path.isfile(input_file):
            raise ValueError("Input file does not exist.")
        output_file = f"{input_file.rsplit('.', 1)[0]}.{output_format}"
        try:
            audio = AudioSegment.from_file(input_file)
            audio.export(output_file, format=output_format)
            return output_file
        except Exception as e:
            raise RuntimeError(f"Failed to convert audio format: {e}")

    def convert_for_whisper(self, input_wav_file: str) -> str:
        """Converts audio files to a format suitable for Whisper transcription.

        Args:
            input_wav_file (str): The path to the input WAV audio file.

        Returns:
            str: The path to the converted audio file.
        """
        if not os.path.isfile(input_wav_file):
            raise ValueError("Input WAV file does not exist.")

        output_file = f"{input_wav_file.rsplit('.', 1)[0]}_whisper.wav"
        try:
            audio = AudioSegment.from_wav(input_wav_file)
            audio = audio.set_frame_rate(16000).set_channels(1)
            audio.export(output_file, format="wav")
            return output_file
        except Exception as e:
            raise RuntimeError(f"Failed to convert audio for Whisper: {e}")
