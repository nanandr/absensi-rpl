import view.view as view
import controller.controller as controller
from view.menu import menu
from model.mata_kuliah import get_mahasiswa

def kelola (data: list) -> None:
    view.div("=")
    print("Mata Kuliah yang dikelola\n")
    view.div("=")
    
    matkuls = []
    for item in data:
        matkuls.append(item["nama"])
    matkuls.append("Kembali")
    nav = menu(matkuls)
    if nav == "Kembali":
        return
    
    matkul = data[matkuls.index(nav)]

    view.div("=")
    print(f"{matkul["nama"]}")
    print(f"Dosen Pengampu: {matkul["dosen"]}")
    view.div("=")
    nav = menu(["Kelola Absensi", "Rekap Absensi", "Kembali"])

    date = controller.request("Tanggal", ["required", "date"])
    # first pick date

    # print(get_mahasiswa(matkul["kode"]))
    view.div("-")
    print("Daftar Mahasiswa: \n")
    view.div("-")
    enrolled = get_mahasiswa(matkul["kode"])
    for i in range(len(enrolled)):
        print(f"[{i+1}] {enrolled[i]["nama"]}")
    # choose indexes
    view.div("-")
    nim = input(f"Pilih Rentang (1-{len(enrolled)}): ")
    
    # choose status
    status = input(f"Status Kehadiran (rentang) (Hadir/Sakit/Izin): ")