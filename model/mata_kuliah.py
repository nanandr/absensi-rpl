import csv
import model.model as model

path = "data/mata_kuliah.csv"
enrollment_path = "data/mahasiswa_mata_kuliah.csv"
student_path = "data/mahasiswa.csv"

def all () -> list:
    return model.read(path)

def find (key: str, val: any) -> list:
    return model.find(path, key, val)

def create (nama: str,kode: str,dosen: str,kode_dosen: str,sks: int,pj: str):
    matkul = {
        "nama": nama,
        "kode": kode,
        "dosen": dosen,
        "kode_dosen": kode_dosen,
        "sks": sks,
        "pj": pj
    }
    
    data = all()
    data.append(matkul)

    model.save(data)

def enroll (nim: str, kelas: str) -> dict:
    data = [{"nim": nim, "kelas": kelas}]
    model.append(enrollment_path, data)

    return data

def get_mahasiswa (matkul: str) -> list:
    enrolled = model.read(enrollment_path)
    data = model.read(student_path)
    enrolled_mahasiswa = [item["nim"] for item in enrolled if item["kode"] == matkul]
    
    return [mahasiswa for mahasiswa in data if mahasiswa["nim"] in enrolled_mahasiswa]