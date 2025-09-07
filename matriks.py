class Matrix:
    """ 
    Kelas untuk merepresentasikan objek matriks. 
    """
    def __init__(self, data):
	if not isinstance(data, list) or not all(isinstance(row, list) for row in 
data):
	    raise TypeError("Data harus berupa list of lists.") 
	self.data = data 
	self.rows = len(data) 
	self.cols = len(data[0]) if self.rows > 0 else 0
	if not all(len(row) == self.cols for row in data):
	     raise ValueError("Semua baris harus memiliki jumlah kolom yang sama.") 

def print_matrix(matrix): 
    """ 
    Mencetak isi dari objek matriks. 
    """ 
    for row in matrix.data: 
        print(row)

if __name__ == "__main__": 
    matriks_a = Matrix([[1, 2], [3, 4]]) 
    matriks_b = Matrix([[5, 6], [7, 8]])

    print("Hasil Penjumlahan:") 
    hasil_penjumlahan = add_matrices(matriks_a, matriks_b) 
    print_matrix(hasil_penjumlahan
 
    print("\nHasil Perkalian:") 
    hasil_perkalian = multiply_matrices(matriks_a, matriks_b) 
    print_matrix(hasil_perkalian)
