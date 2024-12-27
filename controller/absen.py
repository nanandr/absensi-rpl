import model.absen
import model.mata_kuliah
import view.absen
import view.absen
import view.view

import controller.controller as controller

def create (user):
    # GET ENROLLED CLASS, PASS TO VIEW
    kelas = model.mata_kuliah.enrolled(user)
    nav = view.absen.enrolled(kelas)
    if nav["val"] == "Kembali":
        return
    i = nav["index"]
    tanggal = view.absen.tanggal(kelas[i]["nama"])
    status = view.absen.status()

    # nim,kode,status,tanggal
    model.absen.create([user], kelas[i]["kode"], status, tanggal)
    print("Data absen berhasil ditambahkan.")

def create_pj (matkul, mahasiswa):
    tanggal = controller.request("Tanggal", ["required", "date"])
    select_range = controller.request(f"Pilih Rentang Mahasiswa (1-{len(mahasiswa)})", ["required", "range"])
    start, end = map(int, select_range.split("-"))
    status = view.absen.status()

    model.absen.create(mahasiswa[start-1:end], matkul["kode"], status, tanggal)
    print("Data absen berhasil ditambahkan.")
    
def rekap (user):
    kelas = model.mata_kuliah.enrolled(user)
    i = view.absen.enrolled(kelas)["index"]
    if i["val"] == "Kembali":
        return
    rekap = model.absen.get([user], kelas[i]["kode"])
    view.absen.rekap(rekap, kelas[i]["nama"])

def rekap_pj (matkul, mahasiswa):
    rekap = model.absen.get(mahasiswa, matkul["kode"])
    view.absen.rekap_pj(rekap, matkul["nama"])