import json
import view.view as view


with open("config.json", "r") as file:
    config = json.load(file)

university_name = config["university_name"]

def guest () -> None:
    view.div("=")
    print("Sistem Absensi Mahasiswa")
    print(university_name)
    view.div("=")

def user () -> None:
    view.div("=")
    print("Dashboard")
    print("Sistem Absensi Mahasiswa")
    view.div("=")