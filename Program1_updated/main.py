
# main.py

from data.mahasiswa import Mahasiswa, DataMahasiswa
from view.input_form import InputForm
from view.mahasiswa import ViewMahasiswa

if __name__ == '__main__':
    data_mahasiswa = DataMahasiswa()

    while True:
        print("\n=== Menu Utama ===")
        print("1. Tambah Mahasiswa")
        print("2. Tampilkan Daftar Mahasiswa")
        print("3. Cari Mahasiswa")
        print("4. Ubah Data Mahasiswa")
        print("5. Hapus Mahasiswa")
        print("0. Keluar")
        pilihan = input("Pilih menu: ")

        if pilihan == '1':
            nim, nama, jurusan = InputForm.input_mahasiswa()
            mahasiswa = Mahasiswa(nim, nama, jurusan)
            data_mahasiswa.tambah_mahasiswa(mahasiswa)
            print("Mahasiswa berhasil ditambahkan.")

        elif pilihan == '2':
            ViewMahasiswa.tampilkan_daftar(data_mahasiswa.daftar_mahasiswa())

        elif pilihan == '3':
            nim = InputForm.input_nim()
            mahasiswa = data_mahasiswa.cari_mahasiswa(nim)
            ViewMahasiswa.tampilkan_detail(mahasiswa)

        elif pilihan == '4':
            nim = InputForm.input_nim()
            nama, jurusan = InputForm.input_edit_mahasiswa()
            data_mahasiswa.ubah_mahasiswa(nim, nama, jurusan)
            print("Data mahasiswa berhasil diubah.")

        elif pilihan == '5':
            nim = InputForm.input_nim()
            data_mahasiswa.hapus_mahasiswa(nim)
            print("Mahasiswa berhasil dihapus.")

        elif pilihan == '0':
            print("Keluar dari program.")
            break

        else:
            print("Pilihan tidak valid.")
