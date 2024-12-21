import model.model as model

path = "data/mahasiswa.csv"

def all () -> list:
    return model.read(path)

def find (key: str, val: any) -> list:
    return model.find(path, key, val)

def create (nama: str,nim: int,password: str):
    mahasiswa = {
        "nama": nama,
        "nim": nim,
        "password": password,
    }
    
    data = all()
    data.append(mahasiswa)

    model.save(data)