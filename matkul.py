from ui.divider import div
from model.mata_kuliah import mata_kuliah

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

def join ():
    found = False
    while not found:
        print("Gabung Mata Kuliah")
        kode = input("Kode\t\t\t: ")
        div(1)
        for i in range(len(mata_kuliah)):
                if mata_kuliah[i]["kode"] == kode:
                    found = True
                    print(f"Selamat datang di mata kuliah {mata_kuliah[i]['nama']}")
                    break
                elif i == len(mata_kuliah)-1:
                    print("Tidak dapat menemukan mata kuliah \n")


     