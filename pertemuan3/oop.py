class Buku:
    def __init__(self, nama, tahun, pengarang, halaman, baca=0):
        self.nama = nama
        self.tahun = tahun
        self.pengarang = pengarang
        self.halaman = halaman
        self.baca = baca
    
    def infoBuku(self):
        print(f"{self.nama} diterbitkan tahun {self.tahun}, pengarang {self.pengarang} dengan banyak halaman {self.halaman}")
    
    def setHalamanBacaan(self, banyak):
        self.baca = banyak
    
    def halamanBacaanSekarang(self):
        print(f"Sekarang sudah membaca {self.baca} dari {self.halaman} halaman")

kodingCPP = Buku("Tutorial Koding C++", 2000, "Pak Dengklek", 200)
kodingJava = Buku("Tutorial Koding Java", 2002, "Buk Reni", 300)
kodingPython = Buku("Tutorial Koding Python", 2003, "Pak Rudi", 400)

kodingCPP.halaman = 213

kodingCPP.infoBuku()
kodingCPP.setHalamanBacaan(2)
kodingCPP.halamanBacaanSekarang()