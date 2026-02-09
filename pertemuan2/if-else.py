a = 67
b = 69
if b > a:
    print("b besar dari a")

number = 15
if number > 0:
    print("Bilangan poitif")

##

a = 67
b = 67
if b > a:
    print("b besar dari a")
elif a == b:
    print("a dan b sama")

##

a = 123
b = 22
if b > a:
    print("b besar dari a")
elif a == b:
    print("a dan b sama")
else:
    print("a besar dari b")


a = 300
b = 200
if b > a:
    print("b besar dari a")
else:
    print("b tidak besar dari a")

a = None
if a:
    print("a tidak kosong")
else:
    print("a kosong")

###
a = 28
b = 28
print("A") if a > b else print("=") if a == b else print("B")

a = 300
b = 34
c = 700
if a > b or a > c:
    print("Setidaknya satu kondisi benar")

age = 28
is_student = False
has_discount_code = True

if (age < 18 or age > 65) and not is_student or has_discount_code:
    print("Selamat, Anda dapat diskon!")

temperature = 25
is_sunny = True

if temperature > 20:
    if is_sunny:
        print("Perfect beach weather!")
