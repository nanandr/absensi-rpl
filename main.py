import controller.mata_kuliah as mata_kuliah
import controller.absen as absen
import view.welcome
import controller.auth
from view.menu import menu

def main ():
    user = {}
    authenticated = False

    # Before login
    while not authenticated:
        view.welcome.guest()

        nav = menu(["Login", "Register", "Exit"])["val"]
        if nav == "Login":
            login_data = controller.auth.login()
            if login_data["auth"]:
                authenticated = True
                user = login_data["user"]
        elif nav == "Register":
            signup_data = controller.auth.signup()
            if signup_data["auth"]:
                authenticated = True
                user = signup_data["user"]    
        elif nav == "Exit":
            break

    while authenticated:
        view.welcome.user()

        nav = menu(["Absen", "Lihat Rekap Absen", "Buat Mata Kuliah", "Gabung Mata Kuliah", "Kelola Mata Kuliah", "Logout"])["val"]

        if nav == "Absen":
            absen.create(user)
        elif nav == "Lihat Rekap Absen":
            absen.rekap(user)
        elif nav == "Buat Mata Kuliah":
            mata_kuliah.create(user)
        elif nav == "Gabung Mata Kuliah":
            mata_kuliah.join(user)
        elif nav == "Kelola Mata Kuliah":
            mata_kuliah.select(user)
        elif nav == "Logout":
            authenticated = False
            break
    
main()