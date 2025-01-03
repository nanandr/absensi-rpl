import json
import model.model as model
from datetime import datetime

enrolled_path = "data/mahasiswa_mata_kuliah.csv"
path = "data/absen.csv"

with open("config.json", "r") as file:
    config = json.load(file)

total_weeks = config["total_weeks"]
start_semester = config["start_semester"]

def current_semester ():
    today = datetime.today()
    current_year = today.year

    # get this year's semester
    semesters = [
        datetime.strptime(f"{current_year}-{date}", "%Y-%m-%d") for date in start_semester
    ]

    # determine today's semester
    if today >= semesters[1]:
        return semesters[1]
    else:
        return semesters[0]

def all () -> list:
    return model.read(path)

def find (key: str, val: any) -> list:
    return model.find(path, key, val)

def create (data: list, kelas: str, status: str, tanggal = None) -> list:
    absen = []
    for mahasiswa in data:
        absen.append({
            "nim": mahasiswa["nim"],
            "kode": kelas,
            "status": status,
            "timestamp": f"{model.get_time()} {tanggal if tanggal else model.get_date()}"
            })
        
    model.append(path, absen)
    return absen

# data = user list
def get(data: list, kelas: str) -> list:
    rekap = []
    for mahasiswa in data:
        # { nim, nama, absen: [16] }
        absen = [0] * total_weeks
        data_absen = find("nim", mahasiswa["nim"])

        for entry in data_absen:
            if entry["kode"] == kelas:
                # Parse the date from data_absen
                entry_date = datetime.strptime(entry["timestamp"], "%H:%M:%S.%f %Y-%m-%d")
                # entry_date = timestamp.date()

                # Calculate the week index
                week_index = (entry_date - current_semester()).days // 7

                # Ensure the week index is within range
                if 0 <= week_index < total_weeks:
                    absen[week_index] = entry["status"]

        rekap.append({
            "nim": mahasiswa["nim"],
            "nama": mahasiswa["nama"],
            "absen": absen
        })
    
    return rekap