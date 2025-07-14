"""
Copyright © 2025 Nicolas St-Amour. All rights reserved.
Licensed under the Dub-Suite Source-Available License.

This software is source-available for educational and personal use only.
Commercial use requires explicit written permission.
"""


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
