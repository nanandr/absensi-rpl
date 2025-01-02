import random
import model.model as model

path = "data/mata_kuliah.csv"
enrollment_path = "data/mahasiswa_mata_kuliah.csv"
student_path = "data/mahasiswa.csv"

def all () -> list:
    return model.read(path)

def find (key: str, val: any) -> list:
    return model.find(path, key, val)

def generate_invite_code (kode):
    while True:
        random_digits = random.randint(100000, 999999) # generate 6 digit random int
        invite_code = f"{kode}_{random_digits}"

        if len(find("kode_undangan", invite_code)) == 0:
            break

    return invite_code

def create (data, nim):
    matkul = {
        "id": f"{nim}_{data['kode']}",
        "nama": data["nama"],
        "kode": data["kode"],
        "dosen": f'{data["dosen"]}',
        "kode_dosen": data["kode_dosen"],
        "sks": data["sks"],
        "pj": nim,
        "day": data["day"],
        "time": data["time"],
        "kode_undangan": data["kode_undangan"]
    }

    model.append(path, [matkul])

def edit (kode, data):
    matkuls = all()
    for i, matkul in enumerate(matkuls):
        if matkul["kode"] == kode:
            matkuls[i] = {
                "nama": data["nama"],
                "kode": kode,
                "dosen": f'{data["dosen"]}',
                "kode_dosen": data["kode_dosen"],
                "sks": data["sks"],
                "pj": matkul["pj"],
                "day": data["day"],
                "time": data["time"]
            }
            break
    model.save(path, matkuls)

def enrolled (user: dict) -> list:
    enrolled_class = model.find(enrollment_path, "nim", user["nim"])
    data = []
    for i in range(len(enrolled_class)):
        matkul = find("kode_undangan", enrolled_class[i]["kode"])
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

def is_now (matkul: dict):
    return int(matkul["day"]) == model.get_day() and model.get_time() >= model.get_time(matkul["time"])