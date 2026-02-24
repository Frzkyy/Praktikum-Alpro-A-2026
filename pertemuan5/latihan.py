def tambah_matrix(A, B):
    if len(A) != len(B) or len(A[0]) != len(B[0]):
        print("Matrix salah")
        return  None
    baris, kolom = len(A), len(A[0])
    hasil = [[A[i][j] + B[i][j] for j in range(kolom)] for i in range(baris)]
    return hasil

def kurang_matrix(A, B):
    if len(A) != len(B) or len(A[0]) != len(B[0]):
        print("Matrix salah")
        return  None
    baris, kolom = len(A), len(A[0])
    hasil = [[A[i][j] - B[i][j] for j in range(kolom)] for i in range(baris)]
    return hasil

def kali_skalar(matrix, k):
    hasil = []
    for i in matrix:
        newBaris = [elemen * k for elemen in i]
        hasil.append(newBaris)
    return hasil

def print_matrix(matrix):
    for i in matrix:
        print(i)



A = [[5,3,1],
    [2,8,4],
    [6,0,7]]

B = [[1,2,3],
    [4,5,6],
    [7,8,9]]

C_tambah = tambah_matrix(A, B)
C_kurang = kurang_matrix(A, B)
C_skalar = kali_skalar(A, 4)

print("=" * 15)
print("Penambahan Matrix A dan B")
print_matrix(C_tambah)
print("=" * 15)
print("Pengurangan Matrix A dan B")
print_matrix(C_kurang)
print("=" * 15)
print("Pengalian matrix A dengan skalar 4")
print_matrix(C_skalar)