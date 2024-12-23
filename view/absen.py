import view.view
import controller.controller as controller
from view.menu import menu

def enrolled (data: list):
    matkul = []
    for i in range(len(data)):
        matkul.append(data[i]["nama"])
    matkul.append("Kembali")
    
    view.view.div("-")
    print("Daftar Mata Kuliah\n")
    view.view.div("-")
    nav = menu(matkul)

    return nav

def tanggal (kelas: str):
    view.view.div("-")
    print(f"Absen {kelas}\n")
    view.view.div("-")

    tanggal = controller.request("Tanggal", ["required", "date"])

    return tanggal
    

def status ():
    print("Kehadiran:")
    status = menu(["Hadir", "Sakit", "Izin"])
    return status["val"]

def rekap (data: list, kelas: str):
    view.view.div("-")
    print(f"Absensi Kelas {kelas} \n")
    view.view.div("-")
    for mahasiswa in data:
        print(f"{mahasiswa["nama"]}: {mahasiswa["absen"]}")

def rekap_pj (mahasiswa: list, kelas: str):
    view.view.div("-")
    print(f"Absensi Kelas {kelas} \n")
    view.view.div("-")
    for i in range(len(mahasiswa)):
        print(f"[{i+1}] {mahasiswa[i]["nama"]}: {mahasiswa[i]["absen"]}")