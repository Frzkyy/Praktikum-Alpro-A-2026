#Contoh 1
print("================= Contoh 1 =====================")
x = 15
y = 4

print(x + y)
print(x - y)
print(x * y)
print(x / y)
print(x % y)
print(x ** y)
print(x // y)

#Contoh 2
print("================= Contoh 2 =====================")
numbers = [1, 2, 3, 4, 5]

if count := len(numbers) > 3:
    print(f"List has {count} elements")

#Contoh 3
print("================= Contoh 3 =====================")
x = 5
y = 3

print(x == y)
print(x != y)
print(x > y)
print(x < y)
print(x >= y)
print(x <= y)

#Contoh 4
print("================= Contoh 4 =====================")
print("---------------- Contoh 4.1 --------------------")
x = 5

print(x > 0 and x < 10)
print("---------------- Contoh 4.2 --------------------")
x = 5

print(x < 5 or x > 10)
print("---------------- Contoh 4.3 --------------------")
x = 5
print(not(x > 3 and x < 10))

#Contoh 5
print("================= Contoh 5 =====================")
print("---------------- Contoh 5.1 --------------------")
x = ["apple", "banana"]
y = ["apple", "banana"]
z = x

print(x is z)
print(x is y)
print(x == y)
print("---------------- Contoh 5.2 --------------------")
x = ["apple", "banana"]
y = ["apple", "banana"]

print(x is not y)   
print("---------------- Contoh 5.3 --------------------")
x = [1, 2, 3]
y = [1, 2, 3]

print(x == y)
print(x is y)

print("================= Contoh 6 =====================")
print("---------------- Contoh 6.1 --------------------")
fruits = ["apple", "banana", "cherry"]

print("banana" in fruits)

print("---------------- Contoh 6.2 --------------------")
fruits = ["apple", "banana", "cherry"]

print("pineapple" not in fruits)

print("---------------- Contoh 6.3 --------------------")
text = "Hello World"

print("H" in text)
print("hello" in text)
print("z" not in text)


print("================= Contoh 7 =====================")
print(6 & 3)
print(6 | 3)
print(6 ^ 3)

print("================= Contoh 8 =====================")
print((6 + 3) - (6 + 3)) 
print(100 + 5 * 3)
print(5 + 4 - 7 + 3) 

print("================= Contoh 9 =====================")

thislist = ["apple", "banana", "cherry"]
thislist.insert(2, "orange")
print(thislist)