"""
Copyright © 2025 Nicolas St-Amour. All rights reserved.
Licensed under the Dub-Suite Source-Available License.

This software is source-available for educational and personal use only.
Commercial use requires explicit written permission.
"""

try:
    from extract_reference import ReferenceExtractor

    __all__ = [
        "ReferenceExtractor",
    ]

except ImportError as e:
    print(f"Error importing ReferenceExtractor: {e}")
    __all__ = []
