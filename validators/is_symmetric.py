from validators.is_square import is_square
def is_symmetric(matrix):
    jumlah_baris = len(matrix)
    jumlah_kolom = len(matrix[0])
    if jumlah_baris != jumlah_kolom:
	return False
    for i in range(jumlah_baris):
	for j in range(jumlah_kolom):
	    if matrix[i][j] != matrix[j][i]:
		return False
    return True
