import os
import librosa
import soundfile as sf
import numpy as np


class ReferenceExtractor:
    def __init__(self, audio_path: str):
        self.audio_path = audio_path
        self.temp_dir = "temp"
        os.makedirs(self.temp_dir, exist_ok=True)

    def _clean_temp_dir(self):
        """Clean up the temporary directory."""
        for file in os.listdir(self.temp_dir):
            file_path = os.path.join(self.temp_dir, file)
            if os.path.isfile(file_path):
                os.remove(file_path)

    def _extract_reference(self, speaker_dict):
        # Ensure the temporary directory is clean before extraction
        self._clean_temp_dir()
        new_speaker_dict = speaker_dict.copy()
        if os.path.isfile(self.audio_path):
            basename, ext = os.path.splitext(os.path.basename(self.audio_path))
            # generate a reference file for each speaker in the dictionary
            for speaker, segments in speaker_dict.items():
                reference_file = os.path.join(
                    self.temp_dir, f"{basename}_{speaker}_reference.wav"
                )
                # grab first speaker timestamp and last speaker timestamp
                timestamps = [segment["start"] for segment in segments]
                if timestamps:
                    # Sort segments by start time to get chronological order
                    sorted_segments = sorted(segments, key=lambda x: x["start"])

                    # Collect audio segments for this speaker
                    speaker_audio_segments = []
                    total_duration = 0
                    sr = None  # Sample rate will be determined by librosa.load

                    for segment in sorted_segments:
                        if total_duration >= 30:
                            break

                        start_time = segment["start"]
                        end_time = segment["end"]
                        segment_duration = end_time - start_time

                        # Load audio segment for this speaker
                        audio_segment, sr = librosa.load(
                            self.audio_path,
                            sr=None,
                            offset=start_time,
                            duration=segment_duration,
                        )

                        speaker_audio_segments.append(audio_segment)
                        total_duration += segment_duration

                    if speaker_audio_segments and sr is not None:
                        # Concatenate all speaker segments
                        concatenated_audio = np.concatenate(speaker_audio_segments)

                        # Trim to exactly 30 seconds if longer
                        if len(concatenated_audio) > 30 * sr:
                            concatenated_audio = concatenated_audio[: int(30 * sr)]

                        # Save reference file
                        sf.write(reference_file, concatenated_audio, sr)
                        print(
                            f"Reference for {speaker} saved to {reference_file} ({len(concatenated_audio)/sr:.2f}s)"
                        )
                        new_speaker_dict[speaker]["reference"] = reference_file
                    else:
                        print(f"No valid audio segments found for {speaker}.")
                else:
                    print(f"No timestamps found for speaker {speaker}. Skipping.")

            return new_speaker_dict

        else:
            print(f"Audio file {self.audio_path} not found.")
