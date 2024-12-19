import view.view as view
from view.menu import menu

def kelola (data: list) -> None:
    view.div("=")
    print("Mata Kuliah yang dikelola\n")
    view.div("=")
    matkul = []
    for item in data:
        matkul.append(item["nama"])
    matkul.append("Kembali")
    nav = menu(matkul)