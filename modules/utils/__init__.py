"""
Copyright © 2025 Nicolas St-Amour. All rights reserved.
Licensed under the Dub-Suite Source-Available License.

This software is source-available for educational and personal use only.
Commercial use requires explicit written permission.
"""

try:
    from audio_utils import AudioUtils
    from language_detector import LanguageDetector
    from video_audio_extractor import VideoAudioExtractor
    from align_speaker_with_transcription import SpeakerTranscriptionAligner
    from separate_speakers import SpeakerSeparator
    from separate_sfx_vocals import DemucsSFXSeparator
    from translate import Translator

    __all__ = [
        "AudioUtils",
        "LanguageDetector",
        "VideoAudioExtractor",
        "SpeakerTranscriptionAligner",
        "SpeakerSeparator",
        "DemucsSFXSeparator",
        "Translator",
    ]

except ImportError as e:
    print(f"Error importing modules: {e}")
    __all__ = []
