"""
Copyright © 2025 Nicolas St-Amour. All rights reserved.
Licensed under the Dub-Suite Source-Available License.

This software is source-available for educational and personal use only.
Commercial use requires explicit written permission.
"""

try:
    from audio import Transcriber
    from audio import SpeakerDiarization
    from voice import ReferenceExtractor
    from utils import AudioUtils
    from utils import LanguageDetector
    from utils import VideoAudioExtractor
    from utils import SpeakerTranscriptionAligner
    from utils import SpeakerSeparator
    from utils import DemucsSFXSeparator
    from utils import Translator

    __all__ = [
        "Transcriber",
        "AudioUtils",
        "LanguageDetector",
        "VideoAudioExtractor",
        "SpeakerTranscriptionAligner",
        "SpeakerSeparator",
        "DemucsSFXSeparator",
        "Translator",
        "ReferenceExtractor",
        "SpeakerDiarization",
    ]

except ImportError as e:
    print(f"Error importing modules: {e}")
