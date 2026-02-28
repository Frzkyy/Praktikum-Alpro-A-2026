def kali_skalar(matrix, k):
    hasil = []
    for i in matrix:
        newBaris = [elemen * k for elemen in i]
        hasil.append(newBaris)
    return hasil

def transpose(matrix):
    baris = len(matrix)
    kolom = len(matrix[0])
    hasil = [[0 for _ in range(baris)] for _ in range(kolom)]
    for i in range(baris):
        for j in range(kolom):
            hasil[j][i] = matrix[i][j]
    return hasil

matrix = [[1,2,3],
          [4,5,6],
          [7,8,9]]

summary = sum(sum(baris) for baris in matrix)
skalar = kali_skalar(matrix, 3)

try:
    value = input("Enter a value: ")
    print(value/value)
except ValueError:
    print("Bad input...")
except ZeroDivisionError:
    print("Very bad input...")
except TypeError:
    print("Very very bad input...")
except:
    print("Booo!")
