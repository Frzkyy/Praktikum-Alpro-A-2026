Hari = 2
match Hari:
    case 1:
        print("Senin")
    case 2:
        print("Selasa")
    case 3:
        print("Rabu")
    case 4:
        print("Kamis")
    case 5:
        print("Jumat")
    case 6:
        print("Sabtu")
    case 7:
        print("Minggu")

bulan = 4
hari = 2
match hari:
    case 1 | 2 | 3 | 4 | 5 if bulan == 4:
        print("A weekday in April")
    case 1 | 2 | 3 | 4 | 5 if bulan == 5:
        print("A weekday in May")
    case _:
        print("No match")