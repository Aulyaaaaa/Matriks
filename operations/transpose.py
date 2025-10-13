# operations/transpose.py
"""
Modul transpose.py
Berfungsi untuk menghitung transpose dari matriks (pertukaran baris ↔ kolom)
"""

import numpy as np
import pandas as pd

def matrix_transpose(matrix_data):
    """
    Menghitung transpose dari matriks (list of lists)
    """
    try:
        matrix = np.array(matrix_data, dtype=float)
        transposed = matrix.T
        return {
            "status": "success",
            "transpose": transposed.tolist()
        }
    except Exception as e:
        return {
            "status": "error",
            "message": f"Terjadi kesalahan: {str(e)}"
        }


def transpose_from_csv(csv_path):
    """
    Membaca file CSV dan menghitung transpose dari data numerik di dalamnya
    """
    try:
        df = pd.read_csv(csv_path, delimiter=';')
        numeric_df = df.select_dtypes(include='number')

        if numeric_df.empty:
            return {"status": "error", "message": "Tidak ada data numerik dalam CSV"}

        matrix = numeric_df.values
        return matrix_transpose(matrix)
    except Exception as e:
        return {"status": "error", "message": f"Gagal membaca CSV: {str(e)}"}


if __name__ == "__main__":
    # Tes lokal
    contoh = [[1, 2, 3], [4, 5, 6]]
    print(matrix_transpose(contoh))

    # Tes dari CSV datasetemas.csv
    result = transpose_from_csv("datasetemas.csv")
    print(result)
