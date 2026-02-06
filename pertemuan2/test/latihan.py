def fizzbuzz_plus(n): # latihan no 1
    for x in range(1, n+1):
        if x % 15 == 0:
            print("FizzBuzz",end="")
        elif x % 3 == 0:
            print("Fizz",end="")
        elif x % 5 == 0:
            print("Buzz",end="")
        else:
            if x % 7 != 0:
                print(x,end="")

        if x % 7 == 0:
            print("Seven",end="")

        print("")

def is_password_valid(password): # latihan no 2
    hurufBesar = False
    angka = False
    if len(password) >= 8:
        for x in password:
            if x == " ":
                return False
            if x.isupper():
                hurufBesar = True
            if x.isnumeric():
                angka = True
        if hurufBesar and angka:
            return True
        else:
            return False
    else:
        return False

def hitung_nilai(tugas,uts,uas): # latihan no 3
    nilai = (tugas * 0.3) + (uts * 0.3) + (uas * 0.4)

    if nilai >= 85:
        grade = "A"
    elif nilai >= 70:
        grade = "B"
    elif nilai >= 55:
        grade = "C"
    elif nilai >= 40:
        grade = "D"
    elif nilai < 40:
        grade = "E"
        
    print(f"Nilai: {nilai}")
    print(f"Grade: {grade}")

fizzbuzz_plus(21)
