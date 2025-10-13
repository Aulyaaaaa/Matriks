# operations/__init__.py
# subpackage for operation modules
# operations/_init_.py
"""
Package operations untuk proyek Matriks.

Berisi fungsi-fungsi operasi pada matriks, seperti:
- Transpose matriks
- Invers matriks
- Regresi linear (prediksi harga emas)
"""

from .transpose import transpose_matrix
from .inverse import inverse_matrix
from .linier_regression import regresi_emas 

__all__ = [
    "transpose_matrix",
    "inverse_matrix",
    "regresi_emas"
]
