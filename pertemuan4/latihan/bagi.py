try:
    nilai1 = int(input("Masukan Angka Yang Ingin Dibagi: "))
    nilai2 = int(input("Masukan Angka Pembagi: "))

    hasil = float(nilai1/nilai2)
except ZeroDivisionError:
    print("Angka pembagi tidak boleh 0!! ")
except ValueError:
    print("Masukan angka yang benar!!")
else:
    print(hasil)