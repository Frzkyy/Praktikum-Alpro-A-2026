def fungsiSaya():
    print("Haloo")

fungsiSaya()

def fungsiGweh():
    return ["TIA", "TIB", "TIC"]

kelas = fungsiGweh()
print(kelas[0])
print(kelas[1])
print(kelas[2]) 

def fungsiAku(*args):
    print("Type:", type(args))
    print("Argumen pertama:", args[0])
    print("Argumen kedua:", args[1])
    print("Semua argumen:", args)

fungsiAku("Joe", "Choo", "Wi") 

def localScope():
    x = 200
    print(x)

localScope() 


x = 200

def globalScope():
    print(x)

globalScope()

print(x)

lambe = lambda a, b : a * b
print(x(5, 6)) 

