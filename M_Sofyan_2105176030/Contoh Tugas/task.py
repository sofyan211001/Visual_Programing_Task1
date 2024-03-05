class Mahasiswa:
    def __init__(self, nama, kelas, prodi, fakultas, tempat_tinggal, asal):
        self.nama = nama
        self.kelas = kelas
        self.prodi = prodi
        self.fakultas = fakultas
        self.tempat_tinggal = tempat_tinggal
        self.asal = asal

    def tampilkan_data(self):
        print("Nama: ", self.nama)
        print("Kelas: ", self.kelas)
        print("Prodi: ", self.prodi)
        print("Fakultas: ", self.fakultas)
        print("Tempat Tinggal: ", self.tempat_tinggal)
        print("Asal: ", self.asal)

mahasiswa = Mahasiswa("M.Sofyan", "2105175030", "Pendidikan Komputer", "Keguruan dan Ilmu Pendidikan", "Kaubun", "Kutai Timur")
mahasiswa.tampilkan_data()

