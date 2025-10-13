# operations/inverse.py
"""
Modul inverse.py
Berfungsi untuk menghitung invers matriks (balikan matriks)
bisa dari input manual maupun file CSV.
"""

import numpy as np
import pandas as pd

def matrix_inverse(matrix_data):
    """
    Menghitung invers dari matriks (list of lists)
    """
    try:
        matrix = np.array(matrix_data, dtype=float)
        rows, cols = matrix.shape

        if rows != cols:
            return {
                "status": "error",
                "message": f"Matriks harus persegi (baris={rows}, kolom={cols})"
            }

        det = np.linalg.det(matrix)
        if np.isclose(det, 0):
            return {
                "status": "error",
                "message": "Matriks tidak memiliki invers karena determinan = 0",
                "determinant": float(det)
            }

        inverse = np.linalg.inv(matrix)
        return {
            "status": "success",
            "determinant": float(det),
            "inverse": inverse.tolist()
        }

    except Exception as e:
        return {
            "status": "error",
            "message": f"Terjadi kesalahan: {str(e)}"
        }


def inverse_from_csv(csv_path):
    """
    Membaca file CSV dan menghitung invers dari data numerik di dalamnya
    """
    try:
        df = pd.read_csv(csv_path, delimiter=';')
        numeric_df = df.select_dtypes(include='number')

        if numeric_df.empty:
            return {"status": "error", "message": "Tidak ada data numerik dalam CSV"}

        matrix = numeric_df.values
        return matrix_inverse(matrix)
    except Exception as e:
        return {"status": "error", "message": f"Gagal membaca CSV: {str(e)}"}


if __name__ == "__main__":
    # Tes lokal
    contoh = [[2, 5], [1, 3]]
    print(matrix_inverse(contoh))

    # Tes dari CSV datasetemas.csv
    result = inverse_from_csv("datasetemas.csv")
    print(result)
