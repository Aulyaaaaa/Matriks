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
from .regression import linear_regression, predict_price  # jika kamu punya file regression.py

_all_ = [
    "transpose_matrix",
    "inverse_matrix",
    "linear_regression",
    "predict_price"
]
