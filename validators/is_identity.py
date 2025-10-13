# validators/is_identity.py
"""
Fungsi untuk memeriksa apakah sebuah matriks adalah matriks identitas.
Matriks identitas memiliki elemen diagonal bernilai 1 dan elemen lainnya 0.
"""

from validators.is_square import is_square

def is_identity(matrix):
    """
    Mengecek apakah matriks adalah matriks identitas.
    
    Parameter:
        matrix (list[list[float]]): matriks 2D
        
    Return:
        bool: True jika identitas, False jika tidak
    """
    if not is_square(matrix):
        return False

    n = len(matrix)
    for i in range(n):
        for j in range(n):
            if i == j and matrix[i][j] != 1:
                return False
            elif i != j and matrix[i][j] != 0:
                return False
    return True
