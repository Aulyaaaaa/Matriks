# validators/__init__.py
"""
Package validators
Berisi fungsi-fungsi untuk memeriksa sifat-sifat matriks:
- is_square: mengecek apakah matriks persegi (NxN)
- is_symmetric: mengecek apakah matriks simetris (A == A^T)
- is_identity: mengecek apakah matriks identitas (1 di diagonal, 0 di luar diagonal)
"""

from .is_square import is_square
from .is_symmetric import is_symmetric
from .is_identity import is_identity

__all__ = ["is_square", "is_symmetric", "is_identity"]
