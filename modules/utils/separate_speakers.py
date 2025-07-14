class SpeakerSeparator:
    def __init__(self, aligned_words: list):
        self.aligned_words = aligned_words

    def separate(self):
        separated_output_dict = {}
        for word in self.aligned_words:
            speaker = word
            if speaker not in separated_output_dict:
                separated_output_dict[speaker] = {}
            timestamp = f"{word['start']} - {word['end']}"
            separated_output_dict[speaker][timestamp] = word["word"]
        return separated_output_dict
