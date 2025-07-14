```markdown
# Dub-Suite 🎬🎙️

**A comprehensive multilingual dubbing and audio processing toolkit**

> ⚠️ **Work in Progress** - This project is currently under active development and may contain incomplete features or unstable functionality.

## Overview

Dub-Suite is an advanced Python-based toolkit designed for automated video dubbing and audio processing. It provides a complete pipeline for extracting audio from videos, performing speech-to-text transcription, translating content, and generating multilingual voice dubbing with speaker diarization and voice cloning capabilities.

## Features

### 🎯 Current Features

-   **Video Audio Extraction**: Extract high-quality audio from video files using FFmpeg
-   **Speech-to-Text Transcription**: Powered by Whisper for accurate transcription
-   **Language Detection**: Automatic detection of source audio language
-   **Audio Source Separation**: Separate vocals from background music/SFX using Demucs
-   **Speaker Diarization**: Identify and separate different speakers in audio
-   **Translation**: Translate transcriptions between languages using Argos Translate
-   **Voice Cloning**: Extract reference audio samples for voice synthesis
-   **Audio Processing Utilities**: Format conversion and optimization tools

### 🚧 In Development

-   **Text-to-Speech Generation**: Multilingual TTS with voice cloning
-   **Audio Mixing and Merging**: Combine generated dubbing with original SFX
-   **Batch Processing**: Process multiple videos simultaneously
-   **Web Interface**: User-friendly GUI for non-technical users
-   **Quality Enhancement**: Advanced audio processing and noise reduction

## Project Structure
```

Dub-Suite/
├── modules/
│ ├── audio/ # Audio processing modules
│ │ ├── transcribe.py # Whisper-based transcription
│ │ ├── diarize_speakers.py # Speaker diarization
│ │ └── generate_tts.py # TTS generation (WIP)
│ ├── utils/ # Utility modules
│ │ ├── video_audio_extractor.py # Video to audio extraction
│ │ ├── language_detector.py # Language detection
│ │ ├── separate_sfx_vocals.py # Audio source separation
│ │ ├── translate.py # Translation services
│ │ ├── audio_utils.py # Audio format utilities
│ │ └── align_speaker_with_transcription.py # Speaker alignment
│ └── voice/ # Voice cloning modules
│ └── extract_reference.py # Reference audio extraction
├── **main**.py # Main application entry point
└── requirements.txt # Python dependencies

````

## Installation

### Prerequisites
- Python 3.9-3.12 (Python 3.13+ not fully supported yet)
- FFmpeg installed and accessible in system PATH
- CUDA-compatible GPU (optional, for faster processing)

### Setup

These instructions will come soon.

## Usage

### Command Line Interface

```bash
python -m dub_suite --video path/to/video.mp4 --language es
```

## Core Components

### 🎵 Audio Processing

-   **`Transcriber`**: Whisper-based speech-to-text with word-level timestamps
-   **`SpeakerDiarization`**: Identify and segment different speakers
-   **`DemucsSFXSeparator`**: Separate vocals from background audio
-   **`AudioUtils`**: Format conversion and audio optimization

### 🌐 Language Processing

-   **`LanguageDetector`**: Automatic language detection for audio files
-   **`Translator`**: Multi-language translation using Argos Translate
-   **`SpeakerTranscriptionAligner`**: Align speaker segments with transcription

### 🎬 Video Processing

-   **`VideoAudioExtractor`**: Extract audio from video files with multiple quality options
-   **`ReferenceExtractor`**: Extract speaker reference samples for voice cloning

## Technical Requirements

### Python Dependencies

```txt
# Core TTS and Audio Processing
faster-whisper>=1.0.0
torch>=2.0.0
librosa>=0.10.0
soundfile>=0.12.0
pydub>=0.25.0

# Video Processing
ffmpy>=0.3.0

# Language Processing
argostranslate>=1.9.0
langdetect>=1.0.9

# Speaker Processing
pyannote.audio>=3.0.0
demucs>=4.0.0

# Utilities
numpy>=1.24.0
scipy>=1.10.0
```

### Hardware Recommendations

-   **CPU**: Multi-core processor (Intel i7/AMD Ryzen 7 or higher)
-   **RAM**: 16GB+ recommended for processing large video files
-   **GPU**: NVIDIA GPU with 8GB+ VRAM for faster Whisper transcription
-   **Storage**: SSD recommended for temporary file processing

## Supported Formats

### Input Formats

-   **Video**: MP4, AVI, MOV, MKV, WebM
-   **Audio**: WAV, MP3, FLAC, M4A, OGG

### Output Formats

-   **Audio**: WAV (16kHz mono for Whisper, 48kHz for high-quality)
-   **Transcription**: JSON with word-level timestamps
-   **Translation**: Text with preserved timing information

## Development Status

### ✅ Completed

-   [x] Video audio extraction with multiple quality options
-   [x] Whisper-based transcription with word timestamps
-   [x] Language detection and translation
-   [x] Speaker diarization and separation
-   [x] Audio source separation (vocals/SFX)
-   [x] Reference audio extraction for voice cloning

### 🚧 In Progress

-   [ ] Text-to-speech generation with voice cloning
-   [ ] Speaker alignment with transcription
-   [ ] Support for M&E (Music & Effects) with separate vocal tracks in video files
-   [ ] Audio mixing and merging with original SFX
-   [ ] Batch processing capabilities
-   [ ] Error handling and logging improvements

### 📋 Planned

-   [ ] Web-based user interface
-   [ ] Cloud deployment options
-   [ ] Performance optimizations
-   [ ] Advanced audio processing features (noise reduction, EQ)

## License

**Source-Available License - Limited Rights**

Copyright © 2025 Nicolas St-Amour

This software is released under a custom source-available license. You are free to view, study, and use the source code for personal, non-commercial purposes only.

### What this means:
- ✅ You can view and study the source code
- ✅ You can use it for personal, non-commercial projects
- ✅ You can report bugs and contribute suggestions
- ✅ You can fork for personal learning (no redistribution)
- ❌ You cannot use it commercially without permission
- ❌ You cannot redistribute modified versions
- ❌ You cannot create competing products based on this code
- ❌ You cannot sublicense or sell the software

### Contributing
We welcome bug reports, feature suggestions, and code contributions through GitHub issues and pull requests. By contributing, you agree that your submissions will be licensed under the same terms as this project.

Full license terms are available in the [LICENSE](LICENSE) file.

## Acknowledgments

-   **Faster-Whisper**: For speech-to-text transcription
-   **Demucs**: For audio source separation
-   **Pyannote**: For speaker diarization
-   **FFmpeg**: For video/audio processing

---

**Note**: This software is in active development. Features may change, and stability is not guaranteed. Use at your own discretion for production applications.


````
