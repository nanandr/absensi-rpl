from login import login
from header.title import title
from header.divider import div

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
    
    user = res["mahasiswa"] #Dictionary akun mahasiswa
    
main()