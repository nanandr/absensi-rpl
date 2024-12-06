from ui.title import title
from ui.divider import div

from login import login
from nav import nav
import matkul

def main ():
    title()
    authenticated = False
    while not authenticated:
        print("Login Sistem Absensi RPL")
        div(0)
        nim = int(input("NIM: "))
        password = input("Password: ")
        div(1)

        res = login(nim, password)
        authenticated = res["authenticated"]
    
    while authenticated:
        navigate_to = nav()
        if navigate_to == 1:
            matkul.create()
        elif navigate_to == 2:
            matkul.join()
        elif navigate_to == 3:
            print("Berhasil logout")
            authenticated = False

    user = res["mahasiswa"] #Dictionary akun mahasiswa

    
main()