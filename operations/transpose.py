# operations/transpose.py
"""
Modul transpose.py
Berfungsi untuk menghitung transpose matriks dari dataset emas (datasetemas.csv)
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
    Membaca file CSV dan menghitung transpose dari data numerik di dalamnya.
    """
    try:
        df = pd.read_csv(csv_path, delimiter=';')

        # Ambil kolom numerik saja
        numeric_df = df.select_dtypes(include='number')

        if numeric_df.empty:
            return {"status": "error", "message": "Tidak ada data numerik dalam CSV"}

        matrix = numeric_df.values
        return matrix_transpose(matrix)
    except Exception as e:
        return {"status": "error", "message": f"Gagal membaca CSV: {str(e)}"}


if __name__ == "__main__":
    # Tes langsung dengan dataset emas kamu
    csv_path = "datasetemas.csv"
    print(f"Menghitung transpose dari file: {csv_path}")
    result = transpose_from_csv(csv_path)
    print(result)
