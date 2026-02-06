i = 2
while i < 7:
    print(i)
    i += 1

i = 2
while i < 7:
    print(i)
    if i == 3:
        break
    i += 1

i = 1
while i < 7:
    i += 1
    if i == 4:
        continue
    print(i)

i = 1
while i < 6:
    print(i)
    i += 1
else:
    print("i tidak kurang dari 6")