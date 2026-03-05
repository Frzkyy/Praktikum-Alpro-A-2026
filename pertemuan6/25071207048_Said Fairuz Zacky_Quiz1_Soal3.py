def printMenu(menu):
    no = 1
    print(f"No.  Menu | Harga")
    for i in menu:
        print(f"{no}. {i[0]} | {i[1]}")
        no += 1

def inputMenu(menu):
    templist = []
    while True:
        try:
            temp = 0
            belanja = int(input("Masukan Menu ke berapa (0 untuk berhenti): "))
            if belanja < 0 or belanja > 5:
                print("[Error] Mohon masukan angka 1-5 saja")
                raise ValueError
            elif belanja == 0:
                print()
                return templist
            else:
                temp = belanja-1
            
            porsi = int(input("Masukan Banyak Porsi: "))
            if porsi == 0:
                print()
                return templist
            else:
                print(f"Berhasil membeli {menu[belanja][0]} Seharga {menu[belanja][1]}")
                templist.append([menu[belanja][0],porsi])
                

            
        except ValueError:
            print("[Error] Mohon Masukan Hanya Angka")

def printPesanan(pesanan, menu):
    print("Daftar Pesanan: ")
    print("No.  Pesanan | Porsi | Harga")
    no = 1
    total = 0
    for i in pesanan:
        harga = 0
        for j in menu:
            if i[0] == j[0]:
                harga = i[1] * j[1]
        print(f"{no}. {i[0]} | {i[1]} | {harga}")
        total += harga
        no += 1
    print("=" * 15)
    print(f"total: {total}")
    print()
    return total

def kasir(total):
    a = True
    while a:
        try:
            uang = int(input("Masukan Uang Pembayaran: "))
            if uang < total:
                print(f"[Error] Uang Pembayaran Kurang dari total, total: {total} uang: {uang}")
            else:
                print("=" * 15)
                print(f"Total Belanja: Rp {total}")
                print(f"Uang Pembayaran: Rp {uang}")
                if uang == total:
                    print("Tidak ada Kembalian")
                else:
                    print(f"Kembalian: Rp {uang - total}")
                print()
                break
        except ValueError:
            print("[Error] Masukan hanya angka")

menu = [["Nasi Goreng", 15000],
        ["Es Teh",5000],
        ["Gorengan", 2000],
        ["Soto", 12000],
        ["Lontong", 10000]]


printMenu(menu)
belanja = inputMenu(menu)
total = printPesanan(belanja, menu)
kasir(total)

