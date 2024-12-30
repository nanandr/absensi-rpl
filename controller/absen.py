import model.absen
import model.mata_kuliah
import view.absen
import view.absen
import view.view

import controller.controller as controller

def create (user):
    kelas = model.mata_kuliah.enrolled(user)
    nav = view.absen.enrolled(kelas)
    if nav["val"] == "Kembali":
        return
    i = nav["index"]
    if model.mata_kuliah.is_now(kelas[i]):
        # bisa absen jika waktu = jadwal matkul
        status = view.absen.status() # if hadir & time > time + sks = telat
        model.absen.create([user], kelas[i]["kode"], status)
        print("Data absen berhasil ditambahkan.")
        return
    else:
        print("Kelas yang anda pilih belum dimulai.")
        return

def create_pj (matkul, mahasiswa):
    tanggal = controller.request("Tanggal", ["required", "date"])
    # timestamp = tanggal + matkul.jadwal
    select_range = controller.request(f"Pilih Rentang Mahasiswa (1-{len(mahasiswa)})", ["required", "range"])
    start, end = map(int, select_range.split("-"))
    status = view.absen.status()

    model.absen.create(mahasiswa[start-1:end], matkul["kode"], status, tanggal)
    print("Data absen berhasil ditambahkan.")
    
def rekap (user):
    kelas = model.mata_kuliah.enrolled(user)
    nav = view.absen.enrolled(kelas)
    if nav["val"] == "Kembali":
        return
    i = nav["index"]
    rekap = model.absen.get([user], kelas[i]["kode"])
    view.absen.rekap(rekap, kelas[i]["nama"])

def rekap_pj (matkul, mahasiswa):
    rekap = model.absen.get(mahasiswa, matkul["kode"])
    view.absen.rekap_pj(rekap, matkul["nama"])