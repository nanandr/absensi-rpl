from ui.title import title
from ui.divider import div

from login import login
from nav import nav

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
            pass
        elif navigate_to == 2:
            pass
        elif navigate_to == 3:
            authenticated = False

    user = res["mahasiswa"] #Dictionary akun mahasiswa

    
main()