import controller.mata_kuliah as mata_kuliah
import view.welcome
from controller.login import login
from view.menu import menu

def main ():
    user = {}
    authenticated = False

    # Before login
    while not authenticated:
        view.welcome.guest()

        nav = menu(["Login", "Register", "Exit"])
        if nav == "Login":
            login_data = login()
            if login_data["auth"]:
                authenticated = True
                user = login_data["user"]
        elif nav == "Register":
            pass
        elif nav == "Exit":
            break

    while authenticated:
        view.welcome.user()

        nav = menu(["Absen", "Lihat Rekap Absen", "Buat Mata Kuliah", "Gabung Mata Kuliah", "Kelola Mata Kuliah", "Logout"])

        if nav == "Buat Mata Kuliah":
            mata_kuliah.create()
        elif nav == "Kelola Mata Kuliah":
            mata_kuliah.kelola(user["nim"])
        elif nav == "Logout":
            authenticated = False
            break
    
main()