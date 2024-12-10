
# view/mahasiswa.py

class ViewMahasiswa:
    @staticmethod
    def tampilkan_daftar(data):
        if not data:
            print("Tidak ada data mahasiswa.")
        else:
            for m in data:
                print(m)

    @staticmethod
    def tampilkan_detail(mahasiswa):
        if mahasiswa:
            print(mahasiswa)
        else:
            print("Mahasiswa tidak ditemukan.")
