import model.model as model

path = "data/mahasiswa.csv"

def all () -> list:
    return model.read(path)

def find (key: str, val: any) -> dict:
    data = model.read(path)
    for item in data:
        if item.get(key) == val:
            return [item]
    return []