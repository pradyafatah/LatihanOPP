
# view/input_form.py

class InputForm:
    @staticmethod
    def input_mahasiswa():
        nim = input("Masukkan NIM: ")
        nama = input("Masukkan Nama: ")
        jurusan = input("Masukkan Jurusan: ")
        return nim, nama, jurusan

    @staticmethod
    def input_nim():
        return input("Masukkan NIM: ")

    @staticmethod
    def input_edit_mahasiswa():
        nama = input("Masukkan Nama baru (kosongkan jika tidak diubah): ")
        jurusan = input("Masukkan Jurusan baru (kosongkan jika tidak diubah): ")
        return nama, jurusan
