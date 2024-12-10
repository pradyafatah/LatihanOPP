
# data/mahasiswa.py

class Mahasiswa:
    def __init__(self, nim, nama, jurusan):
        self.nim = nim
        self.nama = nama
        self.jurusan = jurusan

    def __str__(self):
        return f"NIM: {self.nim}, Nama: {self.nama}, Jurusan: {self.jurusan}"


class DataMahasiswa:
    def __init__(self):
        self.data = []

    def tambah_mahasiswa(self, mahasiswa):
        self.data.append(mahasiswa)

    def hapus_mahasiswa(self, nim):
        self.data = [m for m in self.data if m.nim != nim]

    def ubah_mahasiswa(self, nim, nama=None, jurusan=None):
        for m in self.data:
            if m.nim == nim:
                if nama:
                    m.nama = nama
                if jurusan:
                    m.jurusan = jurusan

    def cari_mahasiswa(self, nim):
        for m in self.data:
            if m.nim == nim:
                return m
        return None

    def daftar_mahasiswa(self):
        return self.data
