"""
Copyright © 2025 Nicolas St-Amour. All rights reserved.
Licensed under the Dub-Suite Source-Available License.

This software is source-available for educational and personal use only.
Commercial use requires explicit written permission.
"""

try:
    from transcribe import Transcriber
    from diarize_speakers import SpeakerDiarization

    __all__ = ["Transcriber", "SpeakerDiarization"]

except ImportError as e:
    print(f"Error importing modules: {e}")
    __all__ = []
