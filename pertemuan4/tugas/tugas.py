class NamaError(Exception):
    def __init__(self, nama):
        self.nama = nama
        super().__init__(f"{self.nama} terlalu singkat, harus lebih dari 3 karakter")

class UmurError(Exception):
    def __init__(self, umur):
        self.umur = umur
        super().__init__(f"Umur {self.umur} tidak memenuhi syarat, harus 17-60 tahun")

class EmailError(Exception):
    def __init__(self, email):
        self.email = email
        super().__init__(f'{email} harus memiliki @')

class NomorError(Exception):
    def __init__(self, nomor):
        self.nomor = nomor
        super().__init__(f"{nomor} tidak valid, harus 10-13 digit angka")
    
def validasiUmur(umur):
    if umur > 60 or umur < 17:
        raise UmurError(umur)
    return True

def validasiNama(nama):
    if len(nama) < 3:
        raise NamaError(nama)
    return True

def validasiEmail(email):
    if not "@" in email:
        raise EmailError(email)
    return True

def validasiNomor(nomor):
    nomor = str(nomor)
    if len(nomor) < 10 or len(nomor) > 13:
        raise NomorError(nomor)
    return True

try:
    while True:
        try:
            nama = input("Masukan Nama: ")
            validasiNama(nama)
        except NamaError as e:
            print(f'[ERROR]: {e}')
        else:
            break
    print(f"Nama: {nama}")
        
    while True:
        try:
            umur = int(input("Masukan Umur: "))
            validasiUmur(umur)
        except UmurError as e:
            print(f"[ERROR]: {e}")
        except ValueError:
            print("[ERROR]: Harus berupa Angka")
        else:
            break
    print(f"Umur: {umur}")

    while True:
        try:
            email = input("Masukan Email: ")
            validasiEmail(email)
        except EmailError as e:
            print(f"[ERROR]: {e}")
        else:
            break
    print(f"Email: {email}")

    while True:
        try:
            nomor = int(input("Masukan Nomor HP: "))
            validasiNomor(nomor)
        except NomorError as e:
            print(f"[ERROR]: {e}")
        except ValueError:
            print("Masukan Hanya Angka")
        else:
            break
    print(f"Nomor HP: {nomor}")
finally:
    print("Proses Input Selesai")

print(f"""
=== DATA PESERTA ===
Nama    : {nama}
Umur    : {umur}
Email   : {email}
No HP   : {nomor}
Status  : TERDAFTAR
""")