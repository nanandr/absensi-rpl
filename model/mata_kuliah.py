import model.model as model

path = "data/mata_kuliah.csv"
enrollment_path = "data/mahasiswa_mata_kuliah.csv"
student_path = "data/mahasiswa.csv"

def all () -> list:
    return model.read(path)

def find (key: str, val: any) -> list:
    return model.find(path, key, val)

def create (data, nim):
    matkul = {
        "nama": data["nama"],
        "kode": data["kode"],
        "dosen": data["dosen"],
        "kode_dosen": data["kode_dosen"],
        "sks": data["sks"],
        "pj": nim
    }

    model.append(path, [matkul])

def enrolled (user: dict) -> list:
    enrolled_class = model.find(enrollment_path, "nim", user["nim"])
    data = []
    for i in range(len(enrolled_class)):
        matkul = find("kode", enrolled_class[i]["kode"])
        data.append(matkul[0])
    return data

def join (nim: str, kelas: str) -> dict:
    data = [{"nim": nim, "kode": kelas}]
    model.append(enrollment_path, data)

    return data

def get_mahasiswa (matkul: str) -> list:
    enrolled = model.read(enrollment_path)
    data = model.read(student_path)
    enrolled_mahasiswa = [item["nim"] for item in enrolled if item["kode"] == matkul]
    
    return [mahasiswa for mahasiswa in data if mahasiswa["nim"] in enrolled_mahasiswa]