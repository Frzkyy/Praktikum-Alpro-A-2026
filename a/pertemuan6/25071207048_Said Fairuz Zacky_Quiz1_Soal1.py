def printMenu(menu):
    no = 1
    print(f"No.  Menu | Harga")
    for i in menu:
        print(f"{no}. {i[0]} | {i[1]}")
        no += 1

def inputMenu():
    while True:
        try:
            belanja = int(input("Masukan Menu ke berapa: "))
            if belanja < 1 or belanja > 5:
                print("[Error] Mohon masukan angka 1-5 saja")
            else:
                return belanja-1
        except ValueError:
            print("[Error] Mohon Masukan Hanya Angka")
        
menu = [["Nasi Goreng", 15000],
        ["Es Teh",5000],
        ["Gorengan", 2000],
        ["Soto", 12000],
        ["Lontong", 10000]]


printMenu(menu)
belanja = inputMenu()
print(f"Berhasil membeli {menu[belanja][0]} Seharga {menu[belanja][1]}")
