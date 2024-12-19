import model.mata_kuliah
import view.mata_kuliah

def create ():
    pass

def update ():
    pass

def delete ():
    pass

def kelola (nim: str):
    matkul = model.mata_kuliah.find("pj", nim)
    view.mata_kuliah.kelola(matkul)