# validators/is_symmetric.py
"""
Fungsi untuk memeriksa apakah sebuah matriks simetris.
Matriks dikatakan simetris jika elemen [i][j] == [j][i].
"""

from validators.is_square import is_square

def is_symmetric(matrix):
    """
    Mengecek apakah matriks simetris.
    
    Parameter:
        matrix (list[list[float]]): matriks 2D
        
    Return:
        bool: True jika simetris, False jika tidak
    """
    if not is_square(matrix):
        return False

    n = len(matrix)
    for i in range(n):
        for j in range(n):
            if matrix[i][j] != matrix[j][i]:
                return False
    return True
