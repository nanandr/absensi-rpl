import view.view as view
import controller.controller as controller
from view.menu import menu
from model.mata_kuliah import get_mahasiswa

def create () -> None:
    view.div("=")
    print("Buat Mata Kuliah\n")
    view.div("=")
    nama = controller.request("Nama Mata Kuliah", ["required"])
    kode = controller.request("Kode Mata Kuliah", ["required"])
    dosen = controller.request("Nama Dosen Pengampu", ["required"])
    kode_dosen = controller.request("Kode Dosen", ["required"])
    sks = controller.request("Jumlah SKS", ["required", "digit"])
    print("Jadwal Mata Kuliah:")
    day = menu(["Senin", "Selasa", "Rabu", "Kamis", "Jumat", "Sabtu", "Minggu"])
    time = controller.request("Jam (HH:MM)", ["required", "time"])

    return {
        "nama": nama,
        "kode": kode,
        "dosen": dosen,
        "kode_dosen": kode_dosen,
        "sks": sks,
        "day": day["index"],
        "time": time
    }
    
def edit (matkul: dict) -> None:
    view.div("=")
    print("Edit Mata Kuliah")
    print(f"{matkul['nama']}")
    view.div("=")
    nama = controller.request("Nama Mata Kuliah", ["required"])
    dosen = controller.request("Nama Dosen Pengampu", ["required"])
    kode_dosen = controller.request("Kode Dosen", ["required"])
    sks = controller.request("Jumlah SKS", ["required", "digit"])
    print("Jadwal Mata Kuliah:")
    day = menu(["Senin", "Selasa", "Rabu", "Kamis", "Jumat", "Sabtu", "Minggu"])
    time = controller.request("Jam (HH:MM)", ["required", "time"])

    return {
        "nama": nama,
        "kode": matkul['kode'],
        "dosen": dosen,
        "kode_dosen": kode_dosen,
        "sks": sks,
        "day": day["index"],
        "time": time
    }

def join () -> dict:
    kode = controller.request("Kode Mata Kuliah", ["required"])
    return {
        "kode": kode
    }


# TODO: ORGANIZE THIS CODE ABSEN PJ
def select (data: list) -> None:
    view.div("-")
    print("Mata Kuliah yang dikelola\n")
    view.div("-")
    
    matkuls = []
    for item in data:
        matkuls.append(item["nama"])
    matkuls.append("Kembali")
    nav = menu(matkuls)

    return nav

def action (matkul: dict):
    view.div("=")
    print(f"{matkul['nama']}")
    print(f"Dosen Pengampu: {matkul['dosen']}")
    print(f"Kode Gabung: {matkul['kode']}")
    view.div("=")
    nav = menu(["Kelola Absensi", "Rekap Absensi", "Edit Mata Kuliah", "Kembali"])
    
    return nav

def daftar_mahasiswa (matkul):
    view.div("-")
    print("Daftar Mahasiswa: \n")
    view.div("-")
    enrolled = get_mahasiswa(matkul["kode"])
    for i in range(len(enrolled)):
        print(f"[{i+1}] {enrolled[i]['nama']}")
    # choose indexes
    view.div("-")

    return enrolled