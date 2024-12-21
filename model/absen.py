import model.model as model

path = "data/absen.csv"

def create (data: list, kelas: str, status: str, tanggal: str) -> list:
    absen = []
    for mahasiswa in data:
        absen.append({
            "nim": mahasiswa["nim"],
            "kelas": kelas,
            "status": status,
            "tanggal": tanggal
            })
        
    model.append(path, absen)
    return absen

