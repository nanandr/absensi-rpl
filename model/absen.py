import model.model as model
from datetime import datetime

enrolled_path = "data/mahasiswa_mata_kuliah.csv"
path = "data/absen.csv"

total_weeks = 16
start_semester = ["02-01", "09-01"]

def current_semester ():
    today = datetime.today()
    current_year = today.year

    # get this year's semester
    semesters = [
        datetime.strptime(f"{current_year}-{date}", "%Y-%m-%d") for date in start_semester
    ]

    # determine today's semester
    current_semester = None
    for semester in semesters:
        if today >= semester:
            current_semester = semester
        else:
            break

    return current_semester

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