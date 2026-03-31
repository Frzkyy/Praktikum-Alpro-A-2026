"""
Program Game Tebak Angka
"""

# ==========================
#       Bagian A
# ==========================

""" Fungsi untuk meminta user menebak angka tertentu, yang dimasukan kedalam parameter"""
def tebak_angka(angka_rahasia, maks_percobaan):
    benar = False
    i = 0
    while i < maks_percobaan:
        tebak = int(input("Masukan Angka Tebakan: "))
        if tebak == angka_rahasia:
            print("Benar!")
            return [True,maks_percobaan - i]
        elif tebak > angka_rahasia:
            print("Angka Terlalu Besar")
            i += 1
        elif tebak < angka_rahasia:
            print("Angka Terlalu Kecil")
            i += 1
    print("Percobaan Habis!!")
    return [False, 0]

""" Fungsi untuk menghitung skor melalui sisa percobaan yang ada (sisa percobaan * 10)"""
def hitung_skor(berhasil, sisa_percobaan):
    if berhasil:
        return sisa_percobaan * 10
    else:
        return 0

""" Fungsi untuk memainkan satu ronde game tebak angka"""
def main_satu_ronde(nama, nomor_ronde):
    DAFTAR_ANGKA = [23, 67, 4, 89, 15, 42, 73, 31, 58, 9]
    angka_rahasia = DAFTAR_ANGKA[nomor_ronde % len(DAFTAR_ANGKA)]
    skor = tebak_angka(angka_rahasia, 7)
    nilai = hitung_skor(skor[0], skor[1])
    return [nama, nilai]

# ==========================
#       Bagian B
# ==========================

""" Menampilan list riwayat bermain, jika tidak ada riwayat akan mecetak "Tidak Ada Riwayat" """
def tampilkan_riwayat(riwayat):
    if riwayat:
        p = 1
        print("========== Riwayat ==========")
        for i in riwayat:
            print(f"{p}. Nama: {i[0]} | Skor: {i[1]}")
            p += 1
    else:
        print("Belum ada riwayat")

# ==========================
#       Bagian C
# ==========================

""" Sorting Selection_Sort agar skor bisa diurutkan dari yang tersbesar ke yang terkecil untuk leaderboard"""
def selection_sort_riwayat(riwayat):
    skor = []
    skor = riwayat.copy()

    n = len(skor)
    for i in range(n):
        min_index = i
        for j in range(i+1, n):
            if skor[j][1] > skor[min_index][1]:
                min_index = j
        skor[min_index], skor[i] = skor[i], skor[min_index]
    return skor

""" Menampilkan Leaderboard, dan menambahkan * pada peringkat pertama"""
def tampilkan_leaderboard(riwayat):
    leader = selection_sort_riwayat(riwayat)
    angka = 1
    print("========== Leaderboard ==========")
    for i in leader:
        if angka == 1:
            print(f"*{angka}. Nama: {i[0]} | Skor: {i[1]}")
        else:
            print(f"{angka}. Nama: {i[0]} | Skor: {i[1]}")
        angka += 1
        
# ==========================
#       Main Program
# ==========================
""" Program utama game """

riwayat = []
noren = 0
while True:
    nama = input("Masukan Nama: ")
    riwayat.append(main_satu_ronde(nama, noren))
    mainn = input("Apakah ingin bermain lagi? (Ketik 'ya' atau 1 untuk melanjutkan): ").lower()
    if mainn == "ya" or mainn == "1":
        noren += 1
    else:
        break

print()
tampilkan_riwayat(riwayat)
print()
tampilkan_leaderboard(riwayat)


