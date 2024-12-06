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
    
    nav()
    user = res["mahasiswa"] #Dictionary akun mahasiswa

    
main()