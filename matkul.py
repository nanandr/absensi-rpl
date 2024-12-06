from ui.divider import div

def create():
    print("Buat Mata Kuliah")
    nama = input("Nama Mata Kuliah\t\t\t: ")
    kode = int(input("Kode Mata Kuliah\t\t\t: "))
    dosen = input("Nama Dosen Pengampu\t\t\t: ")
    kode_dosen = input("Kode Dosen\t\t\t\t: ")
    sks = int(input("Jumlah SKS\t\t\t\t: "))
    pj = input("Nama Penanggung Jawab Mata Kuliah\t: ")

    matkul = {
        "nama"          : nama,
        "kode"          : kode,
        "dosen"         : dosen,
        "kode dosen"    : kode_dosen,
        "sks"           : sks,
        "pj"            : pj,
    },

    div(1)
    print("Berhasil membuat mata kuliah")
    print(f"Kode gabung: {kode}")
