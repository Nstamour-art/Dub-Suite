"""
Copyright © 2025 Nicolas St-Amour. All rights reserved.
Licensed under the Dub-Suite Source-Available License.

This software is source-available for educational and personal use only.
Commercial use requires explicit written permission.
"""

import argostranslate


class Translator:
    def __init__(self, source_language: str, target_language: str):
        if source_language not in argostranslate.get_languages():
            raise ValueError(f"Source language '{source_language}' is not supported.")
        if target_language not in argostranslate.get_languages():
            raise ValueError(f"Target language '{target_language}' is not supported.")
        self.source_language = source_language
        self.target_language = target_language

    def _translate(self, text: str) -> str:
        translated_text = argostranslate.translate(
            text, self.source_language, self.target_language
        )
        return translated_text

    def translate_word_dict(self, word_dict: dict) -> dict:
        translated_dict = {}
        for timestamp, word in word_dict.items():
            translated_word = self._translate(word)
            translated_dict[timestamp] = translated_word
        return translated_dict
