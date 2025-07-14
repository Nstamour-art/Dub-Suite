from modules import (
    Transcriber,
    AudioUtils,
    LanguageDetector,
    VideoAudioExtractor,
    Translator,
    SpeakerTranscriptionAligner,
    SpeakerSeparator,
    DemucsSFXSeparator,
    SpeakerDiarization,
    ReferenceExtractor,
)


class DubSuite:
    """
    Main class to run the Dub Suite processing pipeline.
    """

    def __init__(self):
        self.args = self._get_args()
        # Initialize the processing pipeline components.
        self.video_path = self.args.video
        self.export_language = self.args.language
        if not self.video_path or not self.export_language:
            raise ValueError("Both video path and export language must be provided.")

    def _get_args(self):
        """
        Get command line arguments for the Dub Suite processing pipeline.
        """
        import argparse

        parser = argparse.ArgumentParser(description="Dub Suite Processing Pipeline")
        parser.add_argument("--video", type=str, help="Path to the video file")
        parser.add_argument("--language", type=str, help="Language of output dub file")
        return parser.parse_args()

    def run(self):
        """
        Run the Dub Suite processing pipeline.
        """
        # Extract audio from video
        print("Extracting audio from video...")
        video_audio_extractor = VideoAudioExtractor(self.video_path)
        audio_path = video_audio_extractor.extract_audio_HQ()

        self.audio_channels = video_audio_extractor.get_audio_channels()

        # Detect language of the audio
        language_detector = LanguageDetector()
        source_language = language_detector.detect_language(audio_path)
        print(f"Detected language: {source_language}")

        # Split vocals from SFX
        print("Splitting vocals from SFX...")
        separate_sfx_vocals = DemucsSFXSeparator()
        self.vocal_path, self.sfx_path = separate_sfx_vocals.separate(audio_path)
        print(f"Vocals saved to: {self.vocal_path}")
        print(f"SFX saved to: {self.sfx_path}")

        # Convert vocals to whisper format WAV
        print("Converting vocals to Whisper format...")
        audio_utils = AudioUtils()
        whisper_vocal_path = audio_utils.convert_for_whisper(self.vocal_path)
        print(f"Converted vocals saved to: {whisper_vocal_path}")
        # Transcribe the vocals
        transcriber = Transcriber()
        transcription_dict = transcriber.transcribe(whisper_vocal_path, source_language)
        print(f"Transcription completed.")

        # translate the transcription if needed
        if source_language != self.export_language:
            translator = Translator(source_language, self.export_language)
            translated_transcription_dict = translator.translate_word_dict(
                transcription_dict
            )
            print(f"Translation completed.")
        else:
            translated_transcription_dict = transcription_dict
            print("No translation needed, using original transcription.")

        # Get speaker diarization
        speaker_diarizer = SpeakerDiarization()
        speaker_segments_dict = speaker_diarizer.run(whisper_vocal_path)
        print(f"Speaker diarization completed.")

        # Align speakers with transcription
        aligner = SpeakerTranscriptionAligner(
            speaker_segments_dict, translated_transcription_dict
        )
        aligned_and_translated_transcription_dict = aligner.align()
        print(f"Aligned transcription completed.")

        # Separate speakers
        speaker_separator = SpeakerSeparator(aligned_and_translated_transcription_dict)
        separated_speakers_dict = speaker_separator.separate()
        print(f"Speaker separation completed.")

        # Extract references for voice cloning
        reference_extractor = ReferenceExtractor(whisper_vocal_path)
        speaker_reference_dict = reference_extractor.extract_references(
            separated_speakers_dict
        )
        print(f"Reference extraction completed.")

        generated_dubs = []

        # create a dub file for each speaker
        for speaker, info_dict in separated_speakers_dict.items():
            reference_path = speaker_reference_dict.get(speaker, {}).get("reference")
            if reference_path:
                # Create the dub file using the reference audio
                generate_tts = TTSGenerator(info_dict, reference_path)
                generated_dub_path = generate_tts.create_dub()
                generated_dubs.append(generated_dub_path)
            else:
                print(f"No reference found for {speaker}. Skipping dub file creation.")
        if generated_dubs:
            # Combine all generated dub files into a single output file
            merge = MergeDubFiles(generated_dubs)
            merged_dub_path = merge.combine()
            print(f"Merged dub file created at: {merged_dub_path}")
            # add sfx back in if 2.0 <= self.audio_channels
            if 2.0 <= self.audio_channels:
                merged_dub_with_sfx_path = merge.add_sfx(merged_dub_path, self.sfx_path)
