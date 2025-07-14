import os
import ffmpy
import wave
import subprocess
import json


class VideoAudioExtractor:
    def __init__(self, video_path: str):
        """Initializes the VideoAudioExtractor with the path to the video file.
        Args:
            video_path (str): The path to the video file.
        """
        if not os.path.isfile(video_path):
            raise ValueError("Video file does not exist.")
        self.video_path = video_path
        self.audio_path = os.path.splitext(video_path)[0] + f".wav"

        # Default audio configuration for speech processing
        # Default audio configuration for high quality extraction (preserves original channels)
        self.default_audio_config = {
            "-ar": "48000",  # Sample rate
            "-f": "wav",  # Format
            "-acodec": "pcm_s16le",  # Codec
            "-y": None,  # Overwrite output files without asking
        }

        # Mono audio configuration optimized for speech processing (Whisper)
        self.whisper_audio_config = {
            "-ar": "16000",  # Sample rate (Whisper optimal)
            "-ac": "1",  # Mono channel
            "-f": "wav",  # Format
            "-acodec": "pcm_s16le",  # Codec
            "-af": "loudnorm=I=-16:TP=-1.5:LRA=7",  # Audio filter for loudness normalization
            "-y": None,  # Overwrite output files without asking
        }

    def extract_audio_HQ(self) -> str:
        """Extracts audio from the video file and saves it as a WAV file.
        Returns:
            str: The path to the extracted audio file.
        """

        ff = ffmpy.FFmpeg(
            inputs={self.video_path: None},
            outputs={self.audio_path: self.default_audio_config},
        )
        try:
            ff.run()
        except ffmpy.FFRuntimeError as e:
            raise RuntimeError(f"FFmpeg error: {e}")
        except Exception as e:
            raise RuntimeError(f"Failed to extract audio: {e}")
        if not os.path.isfile(self.audio_path):
            raise RuntimeError("Failed to extract audio from video. File not created.")
        return self.audio_path

    def extract_audio_whisper(self) -> str:
        """Extracts audio from the video file and saves it as a WAV file using Whisper optimization.
        Returns:
            str: The path to the extracted audio file.
        """
        ff = ffmpy.FFmpeg(
            inputs={self.video_path: None},
            outputs={self.audio_path: self.whisper_audio_config},
        )
        try:
            ff.run()
        except ffmpy.FFRuntimeError as e:
            raise RuntimeError(f"FFmpeg error: {e}")
        except Exception as e:
            raise RuntimeError(f"Failed to extract audio: {e}")
        if not os.path.isfile(self.audio_path):
            raise RuntimeError("Failed to extract audio from video. File not created.")
        return self.audio_path
    
    def get_audio_channels(self) -> float:
        """Gets the number of audio channels in the extracted audio file.
        Returns:
            float: The number of audio channels (1.0 for mono, 2.0 for stereo).
        """

        try:
            
            # Use ffprobe to get audio channel information
            cmd = [
            'ffprobe',
            '-v', 'quiet',
            '-print_format', 'json',
            '-show_streams',
            '-select_streams', 'a:0',
            self.video_path
            ]
            
            result = subprocess.run(cmd, capture_output=True, text=True, check=True)
            probe_data = json.loads(result.stdout)
            
            if 'streams' in probe_data and len(probe_data['streams']) > 0:
            audio_stream = probe_data['streams'][0]
            num_channels = audio_stream.get('channels', 1)
            return float(num_channels)
            else:
            raise RuntimeError("No audio stream found in video file")
            
        except subprocess.CalledProcessError as e:
            raise RuntimeError(f"FFprobe error: {e}")
        except json.JSONDecodeError as e:
            raise RuntimeError(f"Failed to parse FFprobe output: {e}")
        except Exception as e:
            raise RuntimeError(f"Failed to get audio channels: {e}")
