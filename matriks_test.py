import time 
from matrix import Matrix
from operations.multiplier import multiply_matrices

def create_sparse_data(size):
    data = [[0]] * size for _ in range(size)]
    data[0][0] = 1
    data[size-1][size-1] = 1
    return data

if __name__ == "__main__"
    print("\n--- Menguji Masalah Performa ---")
    sparse_data_1000 = create_sparse_data(1000)
    mat_a = Matrix(sparse_data_1000)
    mat_b = Matrix(sparse_data_1000)
    start_time = time.time()
    product_mat = multiply_matrices(mat_a, mat_b)
    end_time = time.time()

    print(f"Waktu yang dibutuhkan untuk perkalian: {end_time - star_time:.2f} detik")
