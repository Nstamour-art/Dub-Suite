"""
Copyright © 2025 Nicolas St-Amour. All rights reserved.
Licensed under the Dub-Suite Source-Available License.

This software is source-available for educational and personal use only.
Commercial use requires explicit written permission.
"""

from pyannote.audio import Pipeline


class SpeakerDiarization:
    def __init__(self, model="pyannote/speaker-diarization"):
        self.pipeline = Pipeline.from_pretrained(model)

    def run(self, audio_file: str):
        """
        Run speaker diarization on the given audio file.

        :param audio_file: Path to the audio file to be diarized.
        :return: Diarization result containing speaker segments.
        """
        return self.diarize(audio_file)

    def diarize(self, audio_file: str):
        return self.merge_segments(self.pipeline(audio_file))

    def merge_segments(self, diarization):
        merged_segments = []
        for segment in diarization.itersegments():
            start = segment.start
            end = segment.end
            speaker = diarization[segment].label
            merged_segments.append({"start": start, "end": end, "speaker": speaker})
        return merged_segments
