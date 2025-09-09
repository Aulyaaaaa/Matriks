def is_identity(matrix):
    jumlah_baris = len(matrix)
    jumlah_kolom = len(matrix[0])
    if jumlah_baris != jumlah_kolom:
	return False
    for i in range(jumlah_baris):
	for j in range(jumlah_kolom):
           if i == j and matrix[i][j] != 1:
		return False
	   elif i != j and matrix[i][j] != 0:
		return False
    return True 
