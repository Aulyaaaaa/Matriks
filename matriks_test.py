import time 
from matrix import Matrix
from sparsematrix import SparseMatrix
from operations.multiplier import multiply_matrices
import time

def create_sparse_data(size):
    data = [[0]] * size for _ in range(size)]
    data[0][0] = 1
    data[size-1][size-1] = 1
    return data

if __name__ == "__main__"
    print("\n--- Menguji Solusi dengan SparseMatrix ---")
    sparse_data_1000 = create_sparse_data(1000)
   
    # Perhatikan: kita instansiasi SparseMatrix
    mat_a = Matrix(sparse_data_1000)
    mat_b = Matrix(sparse_data_1000)
  
    print("\n--- Pembuktian OCP dengan Penjumlahan ---")
    # Matriks padat (dense)
    matriks_padat = Matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]]

    # Matriks jarang yang memiliki nilai yang sama
    matriks_jarang = SparseMatrix([[1, 0, 0], [0, 5, 0], [7, 0, 9]])

    # Lakukan penjumlahan matriks padat + matriks jarang 
    # Perhatikan: fungsi 'add_matrices()' tidak diubah sama sekali
    hasil_penjumlahan = add_matrices(matriks_padat, matriks_jarang)

    print("Hasil Penjumlahan Matriks Biasa dan Sparse:")
    print(hasil_penjumlahan)

    start_time = time.time()
    # Perhatikan: fungsi multiply_matrices() tidak berubah sama sekali
    product_mat = multiply_matrices(mat_a, mat_b)
    end_time = time.time()

    print(f"Waktu yang dibutuhkan untuk perkalian: {end_time - star_time:.2f} detik")
