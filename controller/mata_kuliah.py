import controller.mata_kuliah
import model.mata_kuliah
import controller.absen
import view.mata_kuliah
import view.view

def create (user: dict):
    data = view.mata_kuliah.create()
    
    # MODIFY THIS WITH f"{user[nim]}_{data[kode]}"
    if (len(model.mata_kuliah.find("id", f"{user['nim']}_{data['kode']}")) > 0):
        view.view.div("-")
        print("Kode Mata Kuliah sudah dipakai.\n")
        return
    
    invite_code = model.mata_kuliah.generate_invite_code(data["kode"])
    data["kode_undangan"] = invite_code

    model.mata_kuliah.create(data, user["nim"]) # CHECK IF CLASS CODE EXISTS
    # ENROLL PJ TO CLASS
    model.mata_kuliah.join(user["nim"], data["kode_undangan"])
    view.view.div("-")
    print("Berhasil membuat mata kuliah baru")
    # WHEN KELOLA MATKUL SHOW THE INVITE CODE AGAIN
    print(f"Kode Gabung: {invite_code}")

def join (user: dict):
    data = view.mata_kuliah.join()
    # FIND
    matkul = model.mata_kuliah.find("kode_undangan", data["kode"])
    view.view.div("-")
    if len(matkul) > 0:
        # NEED TO FIX THIS
        if any(enrolled["kode_undangan"] == data["kode"] for enrolled in model.mata_kuliah.enrolled(user)):
            print("Anda sudah bergabung di mata kuliah ini.")
            return
        # THIS TOO
        model.mata_kuliah.join(user["nim"], data["kode"])
        print(f"Berhasil Gabung Mata Kuliah: {matkul[0]['nama']}")
    else:
        print("Mata Kuliah tidak ditemukan.")

def select (user: dict):
    # KELOLA/REKAP/KEMBALI
    matkuls = model.mata_kuliah.find("pj", user["nim"])
    # DATA = { matkuls, NAV }
    nav = view.mata_kuliah.select(matkuls)

    if nav["val"] == "Kembali":
        return
    
    matkul = matkuls[nav["index"]]
    action = view.mata_kuliah.action(matkul)

    if action["val"] == "Kelola Absensi":
        enrolled = view.mata_kuliah.daftar_mahasiswa(matkul)
        controller.absen.create_pj(matkul, enrolled)
    elif action["val"] == "Rekap Absensi":
        enrolled = model.mata_kuliah.get_mahasiswa(matkul["kode_undangan"])
        controller.absen.rekap_pj(matkul, enrolled)
    elif action["val"] == "Edit Mata Kuliah":
        data = view.mata_kuliah.edit(matkul)
        model.mata_kuliah.edit(matkul['kode'], data)
        view.view.div("-")
        print("Berhasil mengubah data mata kuliah. \n")
    elif action["val"] == "Kembali":
        return
