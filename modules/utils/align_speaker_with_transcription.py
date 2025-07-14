class SpeakerTranscriptionAligner:
    def __init__(self, diarization, transcription):
        self.diarization = diarization
        self.transcription = transcription

    def align(self):
        aligned_output = []
        for segment in self.diarization:
            speaker = segment["speaker"]
            for timestamp, word in self.transcription.items():
                if segment["start"] <= timestamp <= segment["end"]:
                    aligned_output.append(
                        {
                            "start": segment["start"],
                            "end": segment["end"],
                            "speaker": speaker,
                            "word": word,
                        }
                    )
        return aligned_output
