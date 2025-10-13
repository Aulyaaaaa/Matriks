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

from .transpose import matrix_transpose, transpose_from_csv
from .inverse import matrix_inverse
from .linier_regression import regresi_emas 

__all__ = [
    "matrix_transpose",
    "transpose_from_csv",
    "matrix_inverse",
    "regresi_emas"
]
