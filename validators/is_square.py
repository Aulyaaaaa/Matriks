# validators/is_square.py
"""
Fungsi untuk memeriksa apakah sebuah matriks berbentuk persegi (NxN).
"""

def is_square(matrix):
    """
    Mengecek apakah matriks memiliki jumlah baris dan kolom yang sama.
    
    Parameter:
        matrix (list[list[float]]): matriks 2D
        
    Return:
        bool: True jika persegi, False jika tidak
    """
    if not matrix or not isinstance(matrix, list):
        return False

    jumlah_baris = len(matrix)
    jumlah_kolom = len(matrix[0])

    # pastikan semua baris panjangnya sama
    for baris in matrix:
        if len(baris) != jumlah_kolom:
            return False

    return jumlah_baris == jumlah_kolom
